import threading
import time

# Function to print a message
def print_message(message):
    print(message)
    time.sleep(2)  # Simulate a time-consuming task

# Create threads for concurrent execution
thread1 = threading.Thread(target=print_message, args=("I'm Thread 1",))
thread2 = threading.Thread(target=print_message, args=("I'm Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Execution of Thread 1 and Thread 1 has finished.")
