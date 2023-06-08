from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n, self.cur = n, 1
        self.Zero = Lock()
        self.Even = Lock()
        self.Odd = Lock()
        self.Even.acquire()
        self.Odd.acquire()
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.Zero:
                printNumber(0)
                if self.cur % 2:
                    self.Odd.release()
                else:
                    self.Even.release()    
            self.Zero.acquire()
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n // 2):
            with self.Even:
                printNumber(self.cur)
                self.cur += 1
                self.Zero.release()
            self.Even.acquire()
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n + 1) // 2):
            with self.Odd:
                printNumber(self.cur)
                self.cur += 1
                self.Zero.release()
            self.Odd.acquire()