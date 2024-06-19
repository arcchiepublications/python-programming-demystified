import threading

# Function to print a message
def print_message(msg):
    print(msg)

#Thread message 
message =   "Hi, I'm here from Thread."

# Create a thread
thread = threading.Thread(target=print_message, args=(message,))

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread has finished execution.")
