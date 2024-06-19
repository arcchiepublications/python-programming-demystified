import threading
import time

# Function to print a message
def print_message(message):
    print(message)
    time.sleep(3)  # Simulate a time-consuming task

# Create a thread
thread = threading.Thread(target=print_message, args=("I'm here from thread",), name="CodeThread")

# Set the thread as a daemon thread
thread.setDaemon(True)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

# Check if the thread is alive
if thread.is_alive():
    print("Thread is still running")
else:
    print("Thread has finished execution")

# Get the name of the thread
print("Thread name:", thread.getName())

# Check if the thread is a daemon thread
if thread.isDaemon():
    print("Thread is a daemon thread")
else:
    print("Thread is not a daemon thread")
