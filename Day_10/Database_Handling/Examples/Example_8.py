"""
Shared Resource: counter is a global variable
that is shared between threads.

Lock Creation: counter_lock is a lock object
( Lock class) that will be used to synchronize
access to the counter.

So in this example,the lock is created on the instance of Lock class from the threading module. This lock is used to synchronize access to the shared resource, "counter".

Whenever a thread wants to modify the "counter", it must first acquire the lock using a context manager (with counter_lock:). This ensures that only one thread can modify counter at a time, preventing race conditions. When one thread holds the lock, the other thread must wait until the lock is released before it can proceed with its own modifications to "counter".

"""

import threading
import time

# Shared resource
counter = 0

# Create a lock
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(10):
        # Acquire the lock before accessing the shared resource
        with counter_lock:
            counter += 1
        print("Counter incrementing\t",counter)

def decrement_counter():
    global counter
    for _ in range(10,1,-1):
        # Acquire the lock before accessing the shared resource
        with counter_lock:
            counter -= 1
        print("Counter decrementing\t",counter)

# Create threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=decrement_counter)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()  # try commenting this
thread2.join()  # try commenting this

# there is no guarantee of main thread will
# complete at the end if you don't use "join"

# Final counter value
print("\n\n\n")
print(f"Final counter value: {counter}")