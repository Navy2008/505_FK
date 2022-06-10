from multiprocessing import Lock
from threading import Thread
import time

database_value = 0
# functio increase the original value by 1
def increase(lock):
    global database_value
    lock.acquire() # acquires the lock
    local_copy = database_value

    # processing 
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release() # release the lock

if __name__== "__main__":
    lock=Lock()
    print("start value", database_value)

# these are the two threads
    thread1 = Thread(target = increase, args=(lock,))
    thread2 = Thread(target = increase, args=(lock,))

# This instantiates the two threads
    thread1.start()
    thread2.start()
# blocks execution of main until the process whose join method is called 
    thread1.join()
    thread2.join()
# prints value 
    print('end of value', database_value)
#executes when main completes
    print('end of main')