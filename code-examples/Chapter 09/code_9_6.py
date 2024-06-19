from collections import namedtuple

# Define a namedtuple type called 'Car'
Car = namedtuple('Car', 'color mileage')

# Create an instance of Car
my_car = Car('red', 3812.4)

# Accessing fields
print(my_car.color)
