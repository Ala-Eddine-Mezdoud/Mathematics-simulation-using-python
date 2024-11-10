import numpy as np
import matplotlib.pyplot as plt

# Data for bar chart
skills = ["C++", "Python", "JavaScript", "HTML", "CSS", "MySQL", "PHP", "Node.js", "Express.js"]
skill_levels = [5, 7, 7, 8, 7, 5, 3, 7, 6]

# Data for line chart
rng = np.random.default_rng()
years = [2008 + i for i in range(30)]
weights = [60 + i + rng.random() * -1 for i in range(30)]

# Data for scatter plot
x_data = rng.random(500) * 100
y_data = rng.random(500) * 100

# Data for histogram
ages = np.random.normal(20, 1.5, 1000)

# Plot configuration
plt.figure(figsize=(12, 8))

# Scatter plot
plt.subplot(2, 2, 1)
plt.scatter(x_data, y_data, c="yellow", label="Random Data Points")
plt.title("Random Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.legend()

# Line chart
plt.subplot(2, 2, 2)
plt.plot(years, weights, c="red", marker="o", label="Weight over Years")
plt.title("Weight Variation Over Time")
plt.xlabel("Year")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.legend()

# Bar chart
plt.subplot(2, 2, 3)
plt.bar(skills, skill_levels, color="green")
plt.title("Skill Proficiency Levels")
plt.xlabel("Skills")
plt.ylabel("Proficiency Level")
plt.grid(True)

# Histogram
plt.subplot(2, 2, 4)
plt.hist(ages, bins=20, color="blue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()
