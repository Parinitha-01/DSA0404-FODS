import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'Product_Name': ['Laptop', 'Phone', 'Laptop', 'Tablet',
                     'Phone', 'Laptop', 'Tablet', 'Phone'],
    'Quantity_Sold': [10, 20, 15, 8, 25, 12, 10, 15],
    'Sale_Date': ['2026-09-15', '2026-09-18', '2026-09-20',
                  '2026-09-22', '2026-09-25', '2026-09-28',
                  '2026-09-29', '2026-09-30']
})

# Convert Sale_Date to datetime
sales_data['Sale_Date'] = pd.to_datetime(sales_data['Sale_Date'])

# Filter sales for the past month (September 2026)
start_date = '2026-09-01'
end_date = '2026-09-30'

monthly_sales = sales_data[
    (sales_data['Sale_Date'] >= start_date) &
    (sales_data['Sale_Date'] <= end_date)
]

# Calculate total quantity sold for each product
product_sales = monthly_sales.groupby('Product_Name')['Quantity_Sold'].sum()

# Find the top 5 products
top_5_products = product_sales.sort_values(ascending=False).head(5)

print("Top 5 Products Sold:")
print(top_5_products)
