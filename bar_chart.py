import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Read the data from file using read_csv
medals=pd.read_csv('medals_by_country_2016.csv')

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()