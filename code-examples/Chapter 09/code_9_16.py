from collections import OrderedDict

# Creating an OrderedDict with initial items
inventory = OrderedDict([('apple', 50), ('banana', 25), ('orange', 75)])

# Move 'banana' to the end
inventory.move_to_end('banana')

# Move 'apple' to the beginning
inventory.move_to_end('apple', last=False)

print("Reordered Inventory:", inventory)
