class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Go through the list
        
        If 0, check if prev and later is 1
            if 1, move forward to 2nd index after the 1
            if no, plant (and check if have enough), move to 2nd index after new plant
            
        If 1, move to 2nd index after 1
        
        In the end return false
        
        Time O(n)
        Space O(1)
        
        """
        if n == 0: return True
        
        i = 0
        new_plant = 0
        
        while i < len(flowerbed):
            
            if flowerbed[i] == 1:
                i += 2
                
            else: # 0
                if i+1 < len(flowerbed) and flowerbed[i+1] == 1:
                    i += 3
                elif i-1 >= 0 and flowerbed[i-1] == 1:
                    i += 1
                else: # can plant
                    flowerbed[i] = 1
                    new_plant += 1
                    if new_plant == n:
                        return True
                    i += 2
                    
        return False
                
