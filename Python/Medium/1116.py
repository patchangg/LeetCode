from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            self.zero_lock.acquire()
            printNumber(0)
            if (i % 2) == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(2,self.n+1,2):
            self.even_lock.acquire()
            printNumber(j)
            self.zero_lock.release()


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for k in range(1,self.n+1,2):
            self.odd_lock.acquire()
            printNumber(k)
            self.zero_lock.release()

# Use python threading locks to time when to print the function
# First use the zero lock then for even and odd numbers,
# acquire the lock to continue with the function then release another lock
# to start that function
# O(n),O(1) space
n = 2
