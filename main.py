
import os
import pandas as pd
import matplotlib.pyplot as plt

# --------- Reading all CSV files from data folder ----------

def load_files(path="data"):
    all_data = []
    
    # 1. Check if the 'data' directory exists
    if not os.path.exists(path):
        print(f"Error: The data directory '{path}' was not found.")
        print("Please ensure the 'data' folder is in the same directory as main.py.")
        return pd.DataFrame() 

    # 2. Iterate through files and load
    for file in os.listdir(path):
        if file.endswith(".csv"):
            try:
                full_path = os.path.join(path, file)
                df = pd.read_csv(full_path)
                
                # Data cleaning and prep
                df["building"] = file.replace(".csv","")         # adding which building file is from
                df["timestamp"] = pd.to_datetime(df["timestamp"]) # converting to time format
                all_data.append(df)
            except Exception as e:
                print(f"error reading file: {file}. Details: {e}")
                
    # 3. Handle empty data list gracefully
    if not all_data:
        print("No CSV files were successfully loaded. Cannot continue analysis.")
        return pd.DataFrame() 

    final = pd.concat(all_data)
    return final


# -------- Aggregation ka part (daily, weekly, summary) --------

def daily_total(df):
    # group by date and building
    df["date"] = df["timestamp"].dt.date
    day_data = df.groupby(["date","building"])["kwh"].sum().reset_index()
    return day_data

def weekly_total(df):
    # .dt.isocalendar().week requires pandas >= 1.1.0
    df["week"] = df["timestamp"].dt.isocalendar().week
    week_data = df.groupby(["week","building"])["kwh"].sum().reset_index()
    return week_data

def building_info(df):
    # summary of each building
    return df.groupby("building")["kwh"].agg(["mean","min","max","sum"]).reset_index()


# --------- OOP wala part (Basic student level) ----------

class MeterReading:
    def __init__(self, time, unit):
        self.time = time
        self.unit = unit

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_meter(self,time,unit):
        self.readings.append(MeterReading(time,unit))

    def total_use(self):
        t = 0
        for r in self.readings:
            t += r.unit
        return t


# -------- main working --------

df = load_files()

# CRITICAL FIX: Check if the DataFrame is empty before proceeding
if df.empty:
    print("Script terminated due to missing or unreadable data.")
    exit()

daily_df = daily_total(df)
weekly_df = weekly_total(df)
summary_df = building_info(df)

# ----------- Graph / Dashboard plots ---------------

plt.figure(figsize=(10,5))

# daily trend line plot
for b in df["building"].unique():
    # Resample works best on a DataFrame with a DateTimeIndex, but using 'on="timestamp"' works fine for plotting
    d = df[df["building"]==b].resample("D",on="timestamp")["kwh"].sum()
    plt.plot(d,label=b)

plt.title("Daily Energy Consumption - Campus")
plt.xlabel("Days")
plt.ylabel("kWh Usage")
plt.legend()
# Create 'output' folder if it doesn't exist before saving
os.makedirs("output",exist_ok=True) 
plt.savefig("output/dashboard.png")
plt.close()

# saving files
df.to_csv("output/cleaned_energy_data.csv",index=False)
summary_df.to_csv("output/building_summary.csv",index=False)

# summary text file
with open("output/summary.txt","w") as f:
    f.write("Campus Energy Dashboard Summary\n")
    f.write("--------------------------------\n")
    f.write(f"Total Energy Consumption: {df['kwh'].sum():,.2f} kWh\n") # Added formatting
    f.write(f"Highest Use Building: {summary_df.loc[summary_df['sum'].idxmax(),'building']}\n")

print("Done! Output files saved in /output folder")
