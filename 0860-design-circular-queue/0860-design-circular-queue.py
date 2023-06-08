class MyCircularQueue:
    def __init__(self, k: int):
        self.q=[None]*k
        self.front=-1
        self.rear=-1
        self.k=k
    def enQueue(self, value: int) -> bool:
        x=(self.rear+1)%self.k
        if x==self.front:return False
        self.rear=x
        self.q[x]=value
        if self.front==-1:self.front=x
        return True
    def deQueue(self) -> bool:
        if self.front==self.rear and self.front==-1:return False
        elif self.rear==self.front:
            self.q[self.front]=None
            self.front=self.rear=-1
            return True
        else:
            self.q[self.front]=None
            self.front=(self.front+1)%self.k
            return True
    def Front(self) -> int:
        if self.front==self.rear and self.rear==-1:return -1
        else:return self.q[self.front]
    def Rear(self) -> int:
        if self.front==self.rear and self.rear==-1:return -1
        else:return self.q[self.rear]
    def isEmpty(self) -> bool:
        return self.front==self.rear and self.front==-1
    def isFull(self) -> bool:
        return (self.rear+1)%self.k==self.front
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()