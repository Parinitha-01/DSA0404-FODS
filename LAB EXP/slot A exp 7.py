import pandas as pd

# Create a sample DataFrame
order_data = pd.DataFrame({
    'Customer_ID': [101, 102, 101, 103, 102],
    'Order_Date': ['2026-01-10', '2026-01-12', '2026-01-15',
                   '2026-01-08', '2026-01-20'],
    'Product_Name': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone'],
    'Order_Quantity': [2, 1, 3, 2, 4]
})

# Convert Order_Date to datetime format
order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data.groupby('Customer_ID').size()
print("Orders per customer:")
print(orders_per_customer)

# 2. Average order quantity for each product
avg_quantity = order_data.groupby('Product_Name')['Order_Quantity'].mean()
print("\nAverage quantity per product:")
print(avg_quantity)

# 3. Earliest and latest order dates
earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

print("\nEarliest order date:", earliest_date.date())
print("Latest order date:", latest_date.date())
