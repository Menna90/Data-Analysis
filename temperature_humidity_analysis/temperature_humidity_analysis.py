# temperature_humidity_analysis.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Simulate Sensor Data and Save as CSV
# -------------------------------------------------

# Generate a datetime index with 1-minute intervals over 24 hours (1440 readings)
timestamps = pd.date_range(start='2025-06-23 00:00:00', periods=1440, freq='T')

# Generate a sinusoidal temperature pattern to simulate day-night temperature cycle
# Add random noise to make it more realistic
time_in_hours = np.arange(0, 1440) / 60  # Convert minutes to hours (0 to 24)
temperature = 25 + 5 * np.sin(2 * np.pi * time_in_hours / 24) + np.random.normal(0, 0.5, 1440)

# Simulate humidity as random values between 40% and 70%
humidity = np.random.uniform(40, 70, 1440)

# Create a DataFrame with the simulated data
df = pd.DataFrame({
    'Timestamp': timestamps,
    'Temperature_C': temperature,
    'Humidity_%': humidity
})

# Save the simulated data to a CSV file
df.to_csv('sensor_data.csv', index=False)

# -------------------------------------------------
# Analyze Data with pandas
# -------------------------------------------------

# Load the CSV file back into a DataFrame
data = pd.read_csv('sensor_data.csv')

# Convert the 'Timestamp' column to datetime format for time series operations
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Set 'Timestamp' as the index of the DataFrame
data.set_index('Timestamp', inplace=True)

# Display summary statistics (mean, std, min, max, etc.) for temperature and humidity
print("Summary Statistics:\n", data.describe())

# Plot raw temperature and humidity data over time
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Temperature_C'], label='Temperature (°C)')
plt.plot(data.index, data['Humidity_%'], label='Humidity (%)', alpha=0.6)
plt.title('Temperature and Humidity Over 24 Hours')
plt.xlabel('Time')
plt.ylabel('Readings')
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------------------------
# Rolling Averages and Filtering
# -------------------------------------------------

# Calculate 10-minute rolling averages for temperature and humidity
data['Temp_Rolling'] = data['Temperature_C'].rolling(window=10).mean()
data['Humidity_Rolling'] = data['Humidity_%'].rolling(window=10).mean()

# Filter the data for times when humidity is greater than 65%
high_humidity = data[data['Humidity_%'] > 65]

# Save the filtered high humidity data to a separate CSV file
high_humidity.to_csv('high_humidity.csv')

# Plot the 10-minute rolling averages to visualize smoothed trends
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Temp_Rolling'], label='Rolling Temp (°C)', color='red')
plt.plot(data.index, data['Humidity_Rolling'], label='Rolling Humidity (%)', color='blue', alpha=0.6)
plt.title('10-Minute Rolling Averages')
plt.xlabel('Time')
plt.ylabel('Smoothed Readings')
plt.legend()
plt.tight_layout()

# Save the plot as an image file
plt.savefig('rolling_plot.png')
plt.show()
