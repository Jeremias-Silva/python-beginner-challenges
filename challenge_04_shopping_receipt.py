# Collect item names and prices
item1_name = input("Enter the name of item 1: ")
item1_price = float(input("Enter the price of item 1: "))

item2_name = input("Enter the name of item 2: ")
item2_price = float(input("Enter the price of item 2: "))

item3_name = input("Enter the name of item 3: ")
item3_price = float(input("Enter the price of item 3: "))

# Calculate total
total = item1_price + item2_price + item3_price

# Print formatted receipt
print("\n====== SHOPPING RECEIPT ======")
print(f"{item1_name:<20} ${item1_price:>7.2f}")
print(f"{item2_name:<20} ${item2_price:>7.2f}")
print(f"{item3_name:<20} ${item3_price:>7.2f}")
print("-" * 30)
print(f"{'TOTAL':<20} ${total:>7.2f}")
print("==============================")