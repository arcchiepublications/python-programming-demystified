my_list = [1, 2, 3, 'Python', [4, 5]]
print(my_list[0])  # Outputs 1
print(my_list[3])  # Outputs 'Python'
print(my_list[-1])  # Outputs [4, 5]
my_list.append('new item')
print(my_list)  # Outputs [1, 2, 3, 'Python', [4, 5], 'new item']

my_list.insert(2, 'inserted item')
print(my_list)  # Outputs [1, 2, 'inserted item', 3, 'Python', [4, 5], 'new item']

my_list.remove('Python')
print(my_list)  # Outputs [1, 2, 'inserted item', 3, [4, 5], 'new item']

popped_item = my_list.pop()
print(popped_item)  # Outputs 'new item'
print(my_list)      # Outputs [1, 2, 'inserted item', 3, [4, 5]]


my_list[1] = 'modified item'
print(my_list)  # Outputs [1, 'modified item', 'inserted item', 3, [4, 5]]

another_list = [6, 7, 8]
my_list.extend(another_list)
print(my_list)  # Outputs [1, 'modified item', 'inserted item', 3, [4, 5], 6, 7, 8]

index_of_item = my_list.index('modified item')
print(index_of_item)  # Outputs 1


my_list.append(8)
count_of_8 = my_list.count(8)
print(count_of_8)  # Outputs 2, assuming 8 appears twice in the list



my_list.reverse()
print(my_list)  # Outputs a reversed list


numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Outputs [1, 1, 2, 3, 4, 5, 9]


my_list.clear()
print(my_list)  # Outputs []
