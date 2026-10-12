import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 15000, 12000, 18000, 20000, 25000]

# Create line plot
plt.plot(months, sales, marker='o')

# Add title and labels
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')

# Display plot
plt.show()
