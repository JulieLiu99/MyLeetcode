class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Sort by the units then apply greedy algorithm
        # Time O(nlogn)
        # Space O(n)
        
         
        boxTypes.sort(key = lambda x: -x[1]) # big box first
        units = 0
        
        for box, unit in boxTypes:
            if truckSize > box:
                truckSize -= box
                units += box * unit
            else:
                units += truckSize * unit
                break
                
        return units
