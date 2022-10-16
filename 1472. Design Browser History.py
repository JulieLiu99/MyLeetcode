class BrowserHistory:
    """
    List + Pointer
    Time O(n)
    Space O(n)
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.history[self.i+1:] = [url]
        self.i += 1
        
    def back(self, steps: int) -> str:
        while steps and self.i > 0:
            self.i -= 1
            steps -= 1
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        while steps and self.i < len(self.history)-1:
            self.i += 1
            steps -= 1
        return self.history[self.i]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
