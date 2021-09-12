import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Read the data from file using read_csv
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col=["date"])
# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color="b")

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color="r")

plt.show()