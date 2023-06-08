from threading import Lock
class DiningPhilosophers:
    forks = [Lock() for _ in range(5)]
    even = Lock()
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        i = philosopher
        if i % 2 == 0:
            self.even.acquire()
        right_fork = i
        left_fork = (i+1) % 5
        self.forks[right_fork].acquire()
        self.forks[left_fork].acquire()
        pickRightFork()
        pickLeftFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[right_fork].release()
        self.forks[left_fork].release()
        if i % 2 == 0:
            self.even.release()