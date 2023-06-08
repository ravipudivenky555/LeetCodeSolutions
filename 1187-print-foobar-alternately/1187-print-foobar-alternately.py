from threading import Event, Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.canBar = Event()
        self.canBar.clear()  # not yet ready for bar
        self.canFoo = Event()
        self.canFoo.set()  # ready for foor


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.canFoo.wait()  # wait until ready for foo
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.canFoo.clear()  # that foo is printed
            self.canBar.set()  # now, ready for bar


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.canBar.wait()  # wait until ready for bar         
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.canBar.clear()  # that bar is printed
            self.canFoo.set()  # now, ready for foo