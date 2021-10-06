from threading import Semaphore
from threading import Barrier

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.b = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.h:
            self.b.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.o:
            self.b.wait()
            releaseOxygen()

# Give hydrogen a Semaphore with two tokens so it only releases its lock once
# two calls have been given. Same for oxygen but only 1 token
# Once 3 tokens have been given, the barrier releases the tokens back
water = "HOH"
# Ouput = "HHO"
