import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values
x = np.linspace(0, 10, 100)

# Define three functions with different scales
y1 = np.sin(x)
y2 = np.exp(x)
y3 = np.log(x + 1)  # Adding 1 to avoid log(0)

# Create the first plot and set its axis
fig, ax1 = plt.subplots()

# Plot the first function using blue color
ax1.plot(x, y1, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel('Sin(x)', color='b')

# Create the second plot and share the x-axis with the first plot
ax2 = ax1.twinx()

# Plot the second function using red color
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Exp(x)', color='r')



# Show the plot
plt.show()