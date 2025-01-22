import matplotlib.pyplot as plt
import numpy as np
import random
import csv

# Using Seed value here
np.random.seed(0)

x_values = []
y_values = []

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X ', 'Y'])

    for i in range(100):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        x_values.append(x)
        y_values.append(y)
        writer.writerow([x , y])

print(x, y)

plt.scatter(x_values, y_values)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot')
plt.show()