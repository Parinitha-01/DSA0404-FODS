# Item prices and quantities
prices = [100, 200, 150]
quantities = [2, 1, 3]

# Discount and tax rates
discount_rate = 10  # 10%
tax_rate = 5        # 5%

# Calculate subtotal
subtotal = sum(prices[i] * quantities[i] for i in range(len(prices)))

# Calculate discount
discount = subtotal * discount_rate / 100

# Calculate price after discount
discounted_price = subtotal - discount

# Calculate tax
tax = discounted_price * tax_rate / 100

# Calculate final cost
total_cost = discounted_price + tax

print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Tax: ₹", tax)
print("Total cost: ₹", total_cost)
