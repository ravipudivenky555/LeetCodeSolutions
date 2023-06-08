class MyStack:
    def __init__(self):
        self.stack=[]
        self.helperstack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        while len(self.stack)>1:
            self.helperstack.append(self.stack.pop(0))
        x=self.stack.pop()
        self.stack,self.helperstack=self.helperstack,self.stack
        return x
    def top(self) -> int:
        while len(self.stack)>0:
            x=self.stack.pop(0)
            self.helperstack.append(x)
        self.stack,self.helperstack=self.helperstack,self.stack
        return x
    def empty(self) -> bool:
        return not len(self.stack)>0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()