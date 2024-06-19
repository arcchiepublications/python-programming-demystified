from collections import OrderedDict

orders = OrderedDict()
orders['20201201'] = 'Electronics'
orders['20201202'] = 'Books'
orders['20201203'] = 'Home Appliances'

for order_date, order_item in orders.items():
    print(f"Processing order from {order_date}: {order_item}")
