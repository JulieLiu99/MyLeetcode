class CustomStack:
    
    """
    Use an additional array inc[] to record the increment value.
    inc[i]: for all elements stack[0] ~ stack[i], plus inc[i] when popped from the stack.
    When pop stack[i], inc[i-1]+=inc[i] for the bottom elements.

    O(1) time & space for each function
    
    """

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
