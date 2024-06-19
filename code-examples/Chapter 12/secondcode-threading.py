import threading
import psutil

# This function calculates square of numbers
def cal_num_square(number):
    # Get CPU utilization before calculation
    cpu_before = psutil.cpu_percent(interval=None)

    # Calculate square
    square = number * number
    print(f"Thread {threading.current_thread().name}: The square of {number} is {square}")

    # Get CPU utilization after calculation
    cpu_after = psutil.cpu_percent(interval=None)
    print(f"Thread {threading.current_thread().name}: CPU Utilization: {cpu_after - cpu_before}%")

# Numbers in a List 
# This can be more dynamica by taking input from user
numbers = [2, 4, 8, 32, 256]

# Create threads for calculating squares
threads = []
for number in numbers:
    thread = threading.Thread(target=cal_num_square, args=(number,), name=f"Thread-{number}")
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Calculate total CPU utilization
total_cpu_utilization = sum(psutil.cpu_percent(percpu=True, interval=None))
print(f"Total CPU Utilization: {total_cpu_utilization}%")
