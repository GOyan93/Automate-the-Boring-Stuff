"""
Automate the Boring Stuff
Title: Fantasy Game Inventory
Author: GOyan
Init Date: May 14, 2020
"""

inv = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}


def display_inventory(inventory):
    total = 0
    print("Inventory:\n")
    for k, v in inventory.items():
        print(f"{v} {k}")
        total += v
    print(f"Total number of items: {total}")

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(orig_inv, inv_to_add):
    for item in inv_to_add:
        if item in orig_inv:
            orig_inv[item] += 1
        else:
            orig_inv[item] = 1
    display_inventory(orig_inv)


display_inventory(inv)
add_to_inventory(inv, dragon_loot)
