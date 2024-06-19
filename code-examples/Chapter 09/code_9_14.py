from collections import namedtuple

Customer = namedtuple('Customer', 'name age purchases')
customer1 = Customer('Alice', 30, 3)
customer2 = Customer('Bob', 22, 1)

print(f"{customer1.name} (Age: {customer1.age}) - Purchases: {customer1.purchases}")
print(f"{customer2.name} (Age: {customer2.age}) - Purchases: {customer2.purchases}")
