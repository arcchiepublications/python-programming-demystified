# Creating a tuple
my_tuple = (1, 'a', 3.14)

# Accessing elements
print(my_tuple[1])  # Outputs 'a'
another_tuple = 'Python', 42
print(another_tuple)  # Outputs ('Python', 42)


single_element_tuple = (5,)
print(single_element_tuple)  # Outputs (5,)
name, age = another_tuple
print(name)  # Outputs 'Python'
print(age)  # Outputs 42

# my_tuple[1] = 'b'  # Uncommenting this would raise a TypeError

for item in my_tuple:
    print(item)

tuple_as_key = {(1, 2): "tuple key"}
print(tuple_as_key[(1, 2)])  # Outputs 'tuple key'
