import pandas as pd
import matplotlib.pyplot as plt

# Get data and print a sample
data = pd.read_csv("hubble_data.csv") # Reads CSV data file (automatically parses headers)
print('Data sample:\n',data.head(), '\n') # Print the first 5 rows of data and their headers

# Set the index of the data to the distance column
data.set_index('distance', inplace=True) # Distance is our new x axis

# Plot and show the data
data.plot() # Data is already in the proper x v. y format
plt.show()
