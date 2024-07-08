def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        inventory_dict[item] = max(0, quantity)
    return inventory_dict

# Initialize the inventory
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8,
    "grapes": 15,
    "pears": 7
}

# Update the inventory
for _ in range(3):
    item = input("Enter the item to update: ")
    quantity = int(input("Enter the quantity to add/remove: "))
    inventory = update_inventory(inventory, item, quantity)

print("Updated inventory:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
