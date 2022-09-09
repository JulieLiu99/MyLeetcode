class MinStack:       
    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])]) # maintain current stack min at self.stack[-1][1]

    def pop(self): 
        if len(self.stack) > 1: self.stack.pop()

    def top(self):
        if len(self.stack) == 1: return None
        return self.stack[-1][0]

    def getMin(self): # getMin operations will always be called on non-empty stacks
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
