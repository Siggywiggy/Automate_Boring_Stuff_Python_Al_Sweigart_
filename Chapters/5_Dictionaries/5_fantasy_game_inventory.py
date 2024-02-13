stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragons_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


# displaying inventory
def display_inventory(inventory):
    print("Inventory:")
    items_total = 0
    for key, value in inventory.items():
        print(f"{value} {key}")
        items_total += value

    print(f"Total number of items: {items_total}")


# adding items from a list to inventory dictionary
def add_to_inventory(loot_list, inventory):
    for item in loot_list:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


display_inventory(stuff)
display_inventory(add_to_inventory(dragons_loot, stuff))
