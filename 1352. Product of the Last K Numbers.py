class ProductOfNumbers:
    """
    Similar to prefix sum. We can record the prefix product.
    prefix[i+1]: product from nums[0] to nums[i]
    prefix[j+1]/prefix[i]: product from nums[i] to nums[j]
    [3,0,2,5,4]     
    ^               [1]
     ^              [1,3]
       ^            [1]
         ^          [1,2]
           ^        [1,2,10]
             ^      [1,2,10,40]
    getProduct(2)   20 = 5 * 4 = product([3,0,2,5,4]) / product([3,0,2])
    getProduct(3)   40 = 2 * 5 * 4 = product([3,0,2,5,4]) / product([3,0])
    
    Time O(1) each
    Space O(N)
    """
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0: #  re-initialize to [1]
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix): # either not enough nums or reinitialized from middle 0
            return 0
        return self.prefix[-1] // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
