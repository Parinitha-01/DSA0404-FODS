import numpy as np

# 3x3 matrix
# Each row represents a different product
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [400, 450, 500]
])

# Calculate the average price of all products sold
average_price = np.mean(sales_data)

print("Sales Data:")
print(sales_data)

print("\nAverage price of all products sold:", average_price)
