import numpy as np

# Fuel efficiency of different car models (in MPG)
fuel_efficiency = np.array([25, 30, 35, 40, 45])

# Calculate average fuel efficiency
average = np.mean(fuel_efficiency)
print("Average fuel efficiency:", average, "MPG")

# Fuel efficiency of two car models
car1 = fuel_efficiency[0]  # 25 MPG
car2 = fuel_efficiency[4]  # 45 MPG

# Calculate percentage improvement
improvement = ((car2 - car1) / car1) * 100
print("Percentage improvement:", improvement, "%")
