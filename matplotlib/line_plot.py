import numpy as np
import matplotlib.pyplot as plt

# Set up the random generator and data
rng = np.random.default_rng()
years = [2008 + x for x in range(30)]
weight = [(60 + y + rng.random() * -1) for y in range(30)]

# Set up the figure and subplots
plt.figure(figsize=(12, 6))

# Plot the first graph in the first subplot
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(years, weight, c="red")
plt.title("Solid Line Plot")

# Plot the second graph in the second subplot
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.plot(years, weight, c="red", linestyle="--")
plt.title("Dashed Line Plot")


# Display both plots at once
plt.tight_layout()  # Adjusts spacing between subplots
plt.show()
