import pandas as pd
import matplotlib.pyplot as plt

# Get data and show a preview of it
data = pd.read_csv("wages_hours.csv", sep='\t') # Delimited by a tab
data = data[['AGE', 'RATE']] # The data we actually care about
data = data.sort_values(['AGE']) # Sort the data by age in acsending order
data.set_index('AGE', inplace=True) # Remove index: sets x axis to age
print('Data sample:\n',data.head(), '\n') # Show data sample

# Plot data
data.plot()
plt.show()
