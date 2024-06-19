from collections import Counter

# Creating a Counter from a list
item_counts = Counter(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])

# Update the count for 'apple'
item_counts.update(['apple'])

# Get the count of 'orange'
orange_count = item_counts['orange']

# Display the most common items
common_items = item_counts.most_common(2)

print("Item Counts:", item_counts)
print("Orange Count:", orange_count)
print("Most Common Items:", common_items)
