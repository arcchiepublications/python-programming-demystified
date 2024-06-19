import threading

# Shared resource
shared_resource = 0

# Lock for synchronization
lock = threading.Lock()

# Function to increment the shared resource
def increment():
    global shared_resource
    for _ in range(1000000):
        # Acquire the lock
        lock.acquire()
        shared_resource += 1
        # Release the lock
        lock.release()

# Create multiple threads to increment the shared resource
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final value of the shared resource
print("Final value of shared resource:", shared_resource)
