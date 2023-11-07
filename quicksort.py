import random
from threading import Thread
import time

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return

def quicksort(array):
    if(len(array) < 2):
        return array
    else:
        pivot = array[0]
        less = quicksort([i for i in array[1:] if i <= pivot])
        greater = quicksort([i for i in array[1:] if i > pivot])
        return less + [pivot] + greater
    
def quickersort(array):
    if(len(array) < 2):
        return array
    else:
        pivot = array[0]
        lessThread = ThreadWithReturnValue(target = quicksort, args = ([i for i in array[1:] if i <= pivot],))
        greaterThread = ThreadWithReturnValue(target = quicksort, args = ([i for i in array[1:] if i > pivot],))
        lessThread.start()
        greaterThread.start()
        less = lessThread.join()
        greater = greaterThread.join()
        return less + [pivot] + greater
    
array = [random.randint(0, 100) for i in range(10)]
print(array)
start = time.time()
# print(quicksort(array))
end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")