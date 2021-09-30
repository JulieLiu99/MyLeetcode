class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Brute Force
        
        O(n^2)
        
        """
        # bulbs = [0]*(n+1) # n+1 because the "first action" is at index "-1"
        # for i in range(1,n+1):
        #     for j in range(0,n+1,i):
        #         bulbs[j] = 1 - bulbs[j]
        # return sum(bulbs[1:])
        
        """
        Math 
        
        Initial state is "OFF" for all bulbs.
        We have n bulbs, number them from bulb_#1 to buld_#n.
        A bulb gets switched only at Round(its factor).
        Bulb_#k will be "ON" after being switched for odd number of times (k has odd factors).
        For all positive integers, only perfect square numbers have odd factors.
        
        """
        # res = 0
        # for i in range(1, math.isqrt(n)+1):
        #     if i*i <= n:
        #         res += 1
        # return res
        
        return int(math.sqrt(n))
