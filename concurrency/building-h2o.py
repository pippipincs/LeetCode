from threading import Semaphore
from threading import Barrier
class H2O:
    def __init__(self):
        pass
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.bar.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.bar.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()