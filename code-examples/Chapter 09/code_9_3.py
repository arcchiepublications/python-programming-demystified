from collections import deque

# Create a deque with some initial items
dq = deque(['a', 'b', 'c'])

# Add elements to the end
dq.append('d')
dq.append('e')

# Add elements to the beginning
dq.appendleft('z')

# Remove and return the rightmost item
right = dq.pop()

# Remove and return the leftmost item
left = dq.popleft()

print("Deque:", dq)
print("Rightmost removed:", right)
print("Leftmost removed:", left)
