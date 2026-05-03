import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers: {i}")
    
def print_letters():
    for letter in "abcd":
        time.sleep(2)
        print(f"Letters: {letter}")

# create two threads

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# start the thread
thread1.start()
thread2.start()

t = time.time()

# join threads
thread1.join()
thread2.join()

finished_time = time.time() - t
print(finished_time)