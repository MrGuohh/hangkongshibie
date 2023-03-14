import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.random.randn(100000)
y = np.random.randn(100000)
colors = np.random.rand(100000)
sizes = np.random.rand(100000)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the scatter points with color and size
scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.5)

# Set the x and y limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Set the x and y labels and title
ax.set_xlabel('X Label', fontsize=14)
ax.set_ylabel('Y Label', fontsize=14)
ax.set_title('Scatter Plot', fontsize=16)

# Add a colorbar to show the point sizes
cb = fig.colorbar(scatter)
cb.set_label('Point Size', fontsize=14)

# Show the plot
plt.show()
