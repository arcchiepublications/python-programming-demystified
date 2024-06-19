my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # Outputs 'Alice'
my_dict['location'] = 'New York'

age = my_dict.pop('age')
my_dict['name'] = 'Bob'

for key, value in my_dict.items():
    print(f"{key}: {value}")

nested_dict = {'employee1': {'name': 'Alice', 'age': 25}, 'employee2': {'name': 'Bob', 'age': 30}}
print(nested_dict['employee1']['name'])  # Outputs 'Alice'

print(my_dict.get('age', 'Not available'))  # Outputs 'Not available'

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

my_dict.update({'age': 26, 'email': 'bob@example.com'})

my_dict.clear()
