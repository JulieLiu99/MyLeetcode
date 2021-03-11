class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        """
        Time O(M+N): scanning through the two lists
        Space O(M+N): mamimum size of intersections[]
        
        """
        
        intersections = []
        i = j = 0
    
        while i < len(firstList) and j < len(secondList): 
            
            # Check for intersection
            if firstList[i][0] <= secondList[j][1] and secondList[j][0] <= firstList[i][1]:
                
                intersections.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

            # Move on from the interval with a smaller endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
