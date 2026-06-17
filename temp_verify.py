from models import Customer, FoodItem, Menu, Transaction

# 1. Create Food Items
burger = FoodItem(name="Spicy Burger", price=5.99, category="Meals", popularity_rating=4.8)
soda = FoodItem(name="Large Soda", price=1.99, category="Drinks", popularity_rating=4.2)
cookie = FoodItem(name="Chocolate Cookie", price=0.99, category="Desserts", popularity_rating=4.9)
salad = FoodItem(name="Garden Salad", price=4.50, category="Meals", popularity_rating=3.9)

print("--- Test Menu Collection & Filtering ---")
menu = Menu([burger, soda, cookie, salad])

# Filter by Category
drinks = menu.filter_by_category("Drinks")
print(f"Drinks: {[item.name for item in drinks]} (Expected: ['Large Soda'])")

desserts = menu.filter_by_category("Desserts")
print(f"Desserts: {[item.name for item in desserts]} (Expected: ['Chocolate Cookie'])")

# Sorting by Price
sorted_price = menu.sort_items_by_price()
print(f"Sorted by price (ascending): {[item.name for item in sorted_price]} (Expected: cookie, soda, salad, burger)")

# Sorting by Popularity
sorted_pop = menu.sort_items_by_popularity()
print(f"Sorted by popularity (descending): {[item.name for item in sorted_pop]} (Expected: cookie, burger, soda, salad)")

print("\n--- Test Customer & Transactions ---")
customer = Customer(name="Alice")
print(f"Customer Name: {customer.name}")
print(f"Is real user initially? {customer.verify_real_user()} (Expected: False)")

# Create Transaction
transaction = Transaction(customer=customer, selected_items=[burger, soda])
print(f"Transaction total: {transaction.compute_total()} (Expected: 7.98)")

# Verify purchase history and real user status
print(f"Is real user now? {customer.verify_real_user()} (Expected: True)")
print(f"Number of transactions in history: {len(customer.purchase_history)}")
print(f"First transaction items: {[item.name for item in customer.purchase_history[0].selected_items]}")

