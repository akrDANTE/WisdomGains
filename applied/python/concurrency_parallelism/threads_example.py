import time
from threading import Thread, current_thread

"""
Threads in python are not really parallel, they are concurrent and are scheduled by time slicing. OS decides which thread should run based on scheduling scheme.
In case of python there is GIL which allows only one thread to execute python bytecode at a time, which effectly is not real parallel execution but is concurrent.
To use actual parallelism we use multiprocessing in python.
Threads are useful when we are dealing with blocking I/O and we need isolation between threads.
"""

def fun(count:int, delay:int):
    thread_name = current_thread().name

    for i in range(count):
        print(f"{thread_name} epoch {i}")
        time.sleep(delay)

if __name__ == "__main__":
    thread1 = Thread(target=fun, args=(5, 2), name="thread1")
    thread2 = Thread(target=fun, args=(5, 1), name="thread2", daemon=True)

    thread1.start()
    thread2.start()

    time.sleep(2)
    thread1.join()
    thread2.join()
