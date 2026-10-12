import pandas as pd

# Create a sample DataFrame
property_data = pd.DataFrame({
    'Property_ID': [101, 102, 103, 104, 105],
    'Location': ['Chennai', 'Bangalore', 'Chennai',
                 'Hyderabad', 'Bangalore'],
    'Bedrooms': [3, 5, 4, 6, 2],
    'Area_sqft': [1500, 2500, 1800, 3000, 1200],
    'Listing_Price': [7500000, 12000000, 9000000,
                      15000000, 6000000]
})

# 1. Average listing price in each location
avg_price = property_data.groupby('Location')['Listing_Price'].mean()
print("Average listing price by location:")
print(avg_price)

# 2. Number of properties with more than four bedrooms
count = (property_data['Bedrooms'] > 4).sum()
print("\nProperties with more than four bedrooms:", count)

# 3. Property with the largest area
largest_property = property_data.loc[property_data['Area_sqft'].idxmax()]
print("\nProperty with the largest area:")
print(largest_property)
