# ByteBites Class Design Summary (from bytebites_design.md)
#
# 1. Customer: Tracks user information (name, purchase history) and validates real users.
# 2. FoodItem: Represents menu items with attributes like name, price, category, and popularity.
# 3. Menu: Manages the collection of FoodItems and provides category filtering.
# 4. Transaction: Groups a customer's selected FoodItems and calculates the total cost.

class Customer:
    def __init__(self, name: str, purchase_history: list = None):
        self.name = name.strip() if name else ""
        self.purchase_history = purchase_history if purchase_history is not None else []

    def verify_real_user(self) -> bool:
        # Returns True if the customer has a non-empty name and a history of transactions.
        return bool(self.name) and len(self.purchase_history) > 0

class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

class Menu:
    def __init__(self, items: list[FoodItem] = None):
        self.items = items if items is not None else []

    def filter_by_category(self, category: str) -> list[FoodItem]:
        # Filters and returns a subset of food items that match the specified category.
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_items_by_popularity(self, descending: bool = True) -> list[FoodItem]:
        # Returns all food items sorted by their popularity rating.
        return sorted(self.items, key=lambda x: x.popularity_rating, reverse=descending)

    def sort_items_by_price(self, descending: bool = False) -> list[FoodItem]:
        # Returns all food items sorted by their price.
        return sorted(self.items, key=lambda x: x.price, reverse=descending)

class Transaction:
    def __init__(self, customer: Customer, selected_items: list[FoodItem]):
        self.customer = customer
        self.selected_items = selected_items
        # Automatically record transaction in customer's purchase history
        self.customer.purchase_history.append(self)

    def compute_total(self) -> float:
        # Calculates and returns the sum of the prices of all selected food items in the transaction.
        return sum(item.price for item in self.selected_items)
