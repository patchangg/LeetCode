from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

# Using python threading locks to lock the function until called
# Threads signal each other to know when to release and call the function
# O(n), O(1) space
n = 2
#output = "foobarfoobar"
