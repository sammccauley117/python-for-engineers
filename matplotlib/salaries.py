import numpy as np
import matplotlib.pyplot as plt

# Load x (name) and y (salary) values
salary = np.fromfile('salaries.txt', dtype=int, sep=',') # Load salaries as CSV integers
names = np.genfromtxt('names.txt', dtype='str', delimiter=',') # Load names as CSV strings
x = np.arange(len(names)) # Can't use strings as x axis, thus create a range array

# Configure and plot the salaries
plt.bar(x, salary) # Creates a bar graph
plt.xticks(x, names) # Add name labels to the x ticks
plt.ylabel('Salary [$]') # Y-axis label
plt.xlabel('Name') # X-axis label
plt.title("People's Salaries") # Chart title
plt.show() # Actually display the plot window

# Print statistics
print('Max Salary:', np.max(salary))
print('Min Salary:', np.min(salary))
print('Avg Salary:', np.average(salary))
print('Med Salary:', np.median(salary))
