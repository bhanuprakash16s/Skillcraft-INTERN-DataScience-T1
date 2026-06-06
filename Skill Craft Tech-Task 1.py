# SCT_DS_1.py
# Bar Chart Visualization in Python

import matplotlib.pyplot as plt

# Sample data
subjects = ["Python", "ML", "DBMS", "CN", "Soft Skills"]
classes = [20, 18, 15, 12, 10]

# Plotting bar chart
plt.bar(subjects, classes, color="skyblue", edgecolor="black")

# Adding title and labels
plt.title("Number of Classes per Subject", fontsize=14)
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Number of Classes", fontsize=12)

# Show the chart
plt.show()
