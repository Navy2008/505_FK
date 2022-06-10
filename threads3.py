from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks available

        # do stuff...
        with lock:
            # prevent printing at the same time
            print(f"in {current_thread().name} got {value}")
        # ...

        # when tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 4
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  #  dies when main thread is dead
        t.start()
    
    # fill the queue with value or items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main is done and TCSS is completed')