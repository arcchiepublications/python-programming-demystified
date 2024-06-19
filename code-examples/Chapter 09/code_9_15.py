from collections import deque

tasks = deque(['Task1', 'Task2', 'Task3'])
tasks.appendleft('Urgent Task')

while tasks:
    current_task = tasks.popleft()
    print(f"Processing {current_task}")

tasks.append('End-of-day Task')
