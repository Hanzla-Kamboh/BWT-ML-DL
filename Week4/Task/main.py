# Sample usage
from Module import FoodItem
from Module import Inventory
import datetime


if __name__ == "__main__":
    inv = Inventory()

    # Add food items
    inv.add_food_item(FoodItem("Meat", "Protein", 50, "090078601", datetime.date(2024, 7, 10)))
    inv.add_food_item(FoodItem("Bananas", "Fruit", 20, "022791103", datetime.date(2024, 7, 20)))
    inv.add_food_item(FoodItem("Eggs", "Protein", 30, "927354314", datetime.date(2024, 7, 15)))
    inv.add_food_item(FoodItem("Jam", "Bakery", 20, "128374659", datetime.date(2024, 7, 8)))

    # Edit food item
    inv.edit_food_item("090078601", quantity=15, expiry_date=datetime.date(2024, 7 , 20))

    # Search food item
    searched_item = inv.search_food_item("090078601")
    if searched_item:
        print("\nSearched Item:", searched_item)
    else:
        print("Item not found.")

    # Delete food item
    if inv.delete_food_item("022791103"):
        print("Item deleted successfully.")
    else:
        print("Item not found for deletion.")

    # Display inventory
    inv.display_inventory()

    # Near expiry items
    print("\nNear Expiry Items:")
    for item in inv.near_expiry_items(7):
        print(item)
