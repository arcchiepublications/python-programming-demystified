from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])

print(od1 == od2)  # False, because the order is different
