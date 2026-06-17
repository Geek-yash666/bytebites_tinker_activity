import pytest
from models import Customer, FoodItem, Menu, Transaction
def test_order_totals():
    """Test that transaction compute_total correctly sums non-empty lists of food items."""
    customer = Customer(name="Test User")
    burger = FoodItem(name="Spicy Burger", price=5.99, category="Meals", popularity_rating=4.5)
    soda = FoodItem(name="Large Soda", price=1.99, category="Drinks", popularity_rating=4.0)
    
    transaction = Transaction(customer=customer, selected_items=[burger, soda])
    assert transaction.compute_total() == pytest.approx(7.98)
    assert len(customer.purchase_history) == 1
    assert customer.verify_real_user() is True
def test_empty_totals():
    """Test that a transaction with no food items yields a total of 0.0."""
    customer = Customer(name="Test User")
    transaction = Transaction(customer=customer, selected_items=[])
    assert transaction.compute_total() == 0.0
    assert len(customer.purchase_history) == 1
    # Note: verify_real_user checks name and purchase history length, so it is True even if order is empty
    assert customer.verify_real_user() is True
def test_filtering_menu_items_by_category():
    """Test that Menu.filter_by_category correctly filters items case-insensitively."""
    burger = FoodItem(name="Spicy Burger", price=5.99, category="Meals", popularity_rating=4.5)
    soda = FoodItem(name="Large Soda", price=1.99, category="Drinks", popularity_rating=4.0)
    salad = FoodItem(name="Garden Salad", price=4.50, category="Meals", popularity_rating=3.9)
    
    menu = Menu([burger, soda, salad])
    
    meals = menu.filter_by_category("Meals")
    assert len(meals) == 2
    assert burger in meals
    assert salad in meals
    
    # Check case-insensitivity
    drinks = menu.filter_by_category("drinks")
    assert len(drinks) == 1
    assert soda in drinks
    
    # Check category with no matches
    desserts = menu.filter_by_category("Desserts")
    assert len(desserts) == 0
def test_customer_validation():
    """Test Customer.verify_real_user handles empty names and empty purchase history."""
    empty_customer = Customer(name="")
    assert empty_customer.verify_real_user() is False
    new_customer = Customer(name="Alice")
    assert new_customer.verify_real_user() is False  # No history yet
    
    # Adding a transaction should make the customer verified
    Transaction(customer=new_customer, selected_items=[])
    assert new_customer.verify_real_user() is True