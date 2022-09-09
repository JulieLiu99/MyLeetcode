class MinStack:       
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append([x, min(x, self.stack[-1][1])]) 
        else:
            self.stack.append([x, x])

    def pop(self): 
        if self.stack: 
            self.stack.pop()

    def top(self):
        if self.stack: 
            return self.stack[-1][0]

    def getMin(self): # getMin operations will always be called on non-empty stacks
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
