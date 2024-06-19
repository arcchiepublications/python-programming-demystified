import threading

# This function calculates square of numbers
def cal_num_square(number):
    square = number * number
    print(f"The square of {number} is {square}")

# Numbers in a List 
# This can be more dynamica by taking input from user
numbers = [2, 4, 8, 32, 256]

# Here, create threads for each and individual numbers
threads = []
for number in numbers:
    thread = threading.Thread(target=cal_num_square, args=(number,))
    threads.append(thread)
    thread.start()

# Wait until all threads finished
for thread in threads:
    thread.join()

print("All threads have finished execution")
