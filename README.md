# Campus Energy Use Dashboard

## 📌 Objective
The main objective of this project was to build an end-to-end energy usage dashboard for campus
buildings using Python. The task involved reading multiple raw meter CSV files, cleaning and merging
them, performing daily/weekly aggregations, and finally visualizing the consumption trends.
This project helps understand which building consumes the most energy and how usage varies over time.

## 📂 Dataset Source
The dataset used in this project consists of separate CSV files for each building.  
Each file contains two columns:

- `timestamp` – date and time of meter reading
- `kwh` – electricity consumed in kilowatt-hour  

Sample data was structured manually for demonstration as no direct dataset was provided.
All CSV files were stored in the `/data` folder and automatically loaded using pandas.

Example structure:
data/
├─ building_A.csv
└─ building_B.csv


## 🛠 Methodology (Step-by-step Work Done)
1. Created a project folder with `data/`, `output/`, and `main.py`.
2. Read multiple CSV files and merged them into one DataFrame using pandas.
3. Cleaned the data and added a `building` column to identify each file source.
4. Performed:
   - Daily usage aggregation
   - Weekly consumption aggregation
   - Building-wise summary (mean, min, max, total)
5. Implemented a simple OOP structure:
   - `MeterReading` class for individual readings
   - `Building` class to store readings and calculate total consumption
6. Visualized energy trends using Matplotlib line plot.
7. Exported final results to `/output` folder:
   - `cleaned_energy_data.csv`
   - `building_summary.csv`
   - `summary.txt`
   - `dashboard.png`

## 📊 Insights & Observations
- Both buildings show clear variation in energy usage over days.
- One building had noticeably higher total consumption compared to the other.
- Peak usage times can be identified through daily trend visualization.
- Weekly comparison helps campus administration plan energy saving strategies.
- Dashboard gives a quick view of how electricity is used across buildings.

## 🚀 How to Run the Project


python main.py


After running, all output files will be generated inside the `/output` folder.

## 📁 Output Files
| File Name | Description |
|----------|-------------|
| cleaned_energy_data.csv | merged dataset from all buildings |
| building_summary.csv | summary stats for each building |
| summary.txt | short written report |
| dashboard.png | plotted consumption graph |

---
