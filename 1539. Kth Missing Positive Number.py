class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Keep track of a counter for # missing numbers
        Keep track of the previous number, subtrack it from the current number for the gap
        If arr[i] - prev > 1, there is a gap of arr[i] - prev - 1
        Increment counter
        
        If counter goes exactly to k, target is arr[i] - 1
        If counter goes over k, target is arr[i] - 1 - (counter - k)
        If counter doesn't reach k at end of arr, target is arr[-1] + k - counter
        
        Scenario 1: target missing number in middle
        
        [2,3,4,7,11]
         ^ 1
           ^ ^ ^ 3
                  ^ 6
        [1,5,6,8,9,10,12,13,...]
        
        Scenario 2: target missing number in the end
        
        [1,2,3,4]
        [5,6,7,...]
        
        Time O(n)
        Space O(1)
        
        """
        counter = 0
        prev = 0
        for i in range(len(arr)):
            counter +=  arr[i] - prev - 1
            if counter >= k:
                return arr[i] - 1 - (counter - k)
            prev = arr[i]
            
        return arr[-1] + k - counter
