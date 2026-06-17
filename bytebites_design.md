## Candidate Classes

1. **Customer**: Tracks customer information, including name and past purchase history, to verify they are real users.
2. **FoodItem**: Models individual food items, tracking details like name, price, category, and popularity rating.
3. **Menu**: A collection/list of food items that allows filtering by category (e.g., Drinks or Desserts).
4. **Transaction**: Groups selected food items together, associates them with a customer, and computes the total cost.

## Class Diagram

```mermaid
classDiagram
    class Customer {
        +str name
        +list~Transaction~ purchase_history
        +verify_real_user() bool
    }

    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }

    class Menu {
        +list~FoodItem~ items
        +filter_by_category(category str) list~FoodItem~
    }

    class Transaction {
        +list~FoodItem~ selected_items
        +Customer customer
        +compute_total() float
    }

    Customer "1" --> "*" Transaction : purchase_history
    Transaction "*" --> "*" FoodItem : selected_items
    Transaction "*" --> "1" Customer : belongs to
    Menu "1" --> "*" FoodItem : items
```
