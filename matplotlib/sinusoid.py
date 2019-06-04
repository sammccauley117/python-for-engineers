import numpy as np
import matplotlib.pyplot as plt

# Create x and y arrays
x = np.linspace(0,20,1000) # Array of 1000 linear spaced elements between [0,20]
y1 = np.sin(x) # Sine of each element of x
y2 = np.cos(x) # Cosine of each element of x

# Configure and plot the sin and cos functions
plt.plot(x , y1, "-g", label="sine") # Add green sine wave to plot
plt.plot(x , y2, "-b", label="cos") # Add blue cosine wave to plot
plt.legend(loc="upper right") # Move legend to upper right corner of window
plt.ylim(-2,2) # Limits the y-axis to [-2,2]
plt.show() # Actually display the plot window
