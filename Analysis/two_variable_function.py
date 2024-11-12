import numpy as np
import matplotlib.pyplot as plt

# Define the grid for x and y values
x = np.linspace(-2.5, 2.5, 500)
y = np.linspace(-2.5, 2.5, 500)
X, Y = np.meshgrid(x, y)

# Compute the expressions inside the square roots
Z1 = X**2 + Y**2 - 1  # for sqrt(x^2 + y^2 - 1)
Z2 = 4 - X**2 - Y**2  # for sqrt(4 - x^2 - y^2)

# Define the valid region where both expressions are non-negative
domain = (Z1 >= 0) & (Z2 >= 0)

# Plot the domain
plt.figure(figsize=(8, 8))
plt.contourf(X, Y, domain, levels=1, colors=["lightgreen", "salmon"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Domain of f4(x, y) = sqrt(x^2 + y^2 - 1) + sqrt(4 - x^2 - y^2)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.colorbar(label="Valid Region")
plt.show()
