# 📈 Temperature and Humidity Sensor Data Simulation & Analysis

This Python project simulates environmental sensor data (temperature and humidity) over a 24-hour period, saves it to a CSV file, performs basic analysis, and visualizes the results using `pandas` and `matplotlib`.

## 🗂️ Project Overview

**Filename:** `temperature_humidity_analysis.py`

**Main Features:**

- Simulates realistic temperature and humidity readings for every minute over 24 hours.
- Saves the simulated data into a CSV file.
- Performs statistical analysis using pandas.
- Visualizes raw and smoothed data using matplotlib.
- Filters and saves entries with high humidity.

## 📊 Data Generation

- **Timestamps:** 1440 entries (1 per minute for 24 hours).
- **Temperature:** Modeled as a sinusoidal daily cycle with added Gaussian noise.
- **Humidity:** Random values uniformly distributed between 40% and 70%.

Generated data is stored in: 
  
    ```
    sensor_data.csv
    ```

## 📈 Data Analysis and Visualization

- **Descriptive Statistics:** Displayed using `data.describe()`.
- **Plots:**
  - Temperature and Humidity trends over time.
  - 10-minute rolling average plots for smoothing.
- **Filtering:**
  - Records with humidity > 65% are saved to:

    ```
    high_humidity.csv
    ```

- **Saved Visualization:**
  - Rolling average plot is saved as:

    ```
    rolling_plot.png
    ```

## 🛠️ Requirements

Make sure you have Python installed along with the following libraries:

```bash
pip install numpy pandas matplotlib
