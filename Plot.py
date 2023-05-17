import matplotlib.pyplot as plt
import numpy as np
import subprocess

# Run the regression script and capture the output
output = subprocess.check_output(['python', 'Regression3.1.py'])
output = output.decode('utf-8')  # Convert bytes to string

# Extract the x and y values from the output
lines = output.strip().split('\n')
x = np.array([float(line.split(',')[0]) for line in lines])
y = np.array([float(line.split(',')[1]) for line in lines])

# Plotting the regression analysis output
plt.scatter(x, y, color='b', label='Data points')
plt.plot(x, y, color='r', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Analysis')
plt.legend()
plt.grid(True)

# Displaying the plot
plt.show()