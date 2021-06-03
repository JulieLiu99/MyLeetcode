class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        """
        Approach 0: Naive Greedy TLE
        
        Use a max heap the store all the colors
        Extract max number N
        Increase the answer by N 
        Put N-1 back to the heap
        
        Orders  Heap    Ans
        4      [5, 2]   0
        3      [4, 2]   5
        2      [3, 2]   5+4=9
        1      [2, 2]   9+3=12
        0      [2, 1]   12+2=14
        
        Time O(orders * log(colors))
        Space O(colors)
        
        """
        
        """
        Approach 1: Greedy + Math
        
        Sort the colors in descending order
        Find a group of colosr that have the same number of balls
        Sell them together
        Until the # of balls equal to the next greatest color
        
        Before  After   Ans
        66631   33331   (6+5+4)*3 = 45
        33331   11111   45 + (3+2)*4 = 65
        11111   00000   70 + 1*5 = 70

        Time O(nlogn)
        Space O(1)

        """
        
        # e.g. 8 + 7 + 6 + 5 + 4 ...
        #      ---------  end
        def getSum(start, end):
            return start * (start + 1) // 2 - end * (end + 1) // 2
        
        inventory.sort(reverse=True)
        factor = 1  # how many colors of the same amount
        n = len(inventory)
        i = 0
        ans = 0
        
        while orders > 0:
            # if we can make sale for all factor 
            if i < n-1 and inventory[i] > inventory[i+1] and orders > factor * (inventory[i] - inventory[i+1]):
                ans += factor * getSum(inventory[i], inventory[i+1])
                orders -= factor * (inventory[i] - inventory[i+1])
            
            # if we cannot make sale for all factor
            elif i == n-1 or inventory[i] > inventory[i+1]:
                sell_all_times = orders // factor
                ans += factor * getSum(inventory[i], inventory[i] - sell_all_times)
                remain_orders = orders % factor
                ans += remain_orders * (inventory[i] - sell_all_times)
                break   # orders = 0
                
            # inventory[i] == inventory[i+1]
            i += 1
            factor += 1
            
        mod = 10 ** 9 + 7
        
        return ans % mod
