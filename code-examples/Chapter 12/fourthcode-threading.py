import threading
import psutil

# Function to calculate sum of a large list of numbers
def calculate_sum(start, end):
    # List of numbers
    numbers = range(start, end)

    # Calculate sum
    total_sum = sum(numbers)
    print(f"Thread {threading.current_thread().name}: Sum of numbers from {start} to {end}: {total_sum}")

# Define the range of numbers for each thread
ranges = [(1, 10000000), (10000001, 20000000), (20000001, 30000000)]

# Create threads for calculating sums
threads = []
for start, end in ranges:
    thread = threading.Thread(target=calculate_sum, args=(start, end), name=f"Thread-{start}-{end}")
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Calculate total CPU utilization
total_cpu_utilization = sum(psutil.cpu_percent(percpu=True, interval=0.1))
print(f"Total CPU Utilization: {total_cpu_utilization}%")
