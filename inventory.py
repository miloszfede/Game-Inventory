import random
def add_to_inventory():
    inventory = []
    wheel_of_fortune = ['dagger', 'gold', 'knife', 'sword', 'armor', 'magic wand' ]
    won_item = random.choice(wheel_of_fortune)
    inventory.append(won_item)
    return print(won_item)

add_to_inventory()