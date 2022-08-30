class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        # Greedy
        # Sell from the most abundant balls as they are valued more 
        
        # Sort inventory in reverse order
        # Scan through the inventory
        # Each tiem, sell the difference between highest and next one
        # Time O(nlogn)
        # Space O(1)
        
        # inventory = [2,8,4,10,6] => 10->8->6->4->2->0
        # 10 | 8 | 6 | 4 | 2
        #  8 | 8 | 6 | 4 | 2
        #  6 | 6 | 6 | 4 | 2
        #  4 | 4 | 4 | 4 | 2
        #  2 | 2 | 2 | 2 | 2 
        #  0 | 0 | 0 | 0 | 0 
        
        inventory.sort(reverse = True) # high to low
        inventory += [0] # to sell the least count color
        res = 0
        k = 1 # one color of the highest count
        
        for i in range(len(inventory)-1):
            
            if inventory[i] > inventory[i+1]:
                
                if k * (inventory[i] - inventory[i+1]) <= orders:
                    res += k * (inventory[i] + inventory[i+1] + 1) * (inventory[i] - inventory[i+1]) // 2 # arithmatic sum
                    orders -= k * (inventory[i] - inventory[i+1])
                    if orders == 0: return res % (10**9 + 7)
                    
                else: # don't need all
                    quotient, remainder = divmod(orders, k)
                    res += k * (inventory[i] + inventory[i] - quotient + 1) * quotient // 2 + remainder * (inventory[i] - quotient)
                    return res % (10**9 + 7)
                
            k += 1 # one more color of the same count
