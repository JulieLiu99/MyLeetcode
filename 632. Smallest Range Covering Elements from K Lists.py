"""
Priority Queue

1. Find max from the first elements of all the lists
2. Find min from the first elements of all the lists
3. Find range = max - min
4. Move ahead in the list of min (because we want range to include elements from all lists)
5. Compute max, min and range again

___\__/___|_\_____|__\_|___/__|___\
https://www.youtube.com/watch?v=Fqal25ZgEDo

Time O(n + n * log(number of lists))
Space O(n)

"""

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        # (first element of list, list number, index of the element in list)
        heap = [(List[0], index, 0) for index, List in enumerate(nums)]  
        
        heapq.heapify(heap)         
        
        max_val = max([List[0] for List in nums]) 
        
        smallest_range = -1e5, 1e5                                     
        
        while heap:

            min_val, list_index, num_index = heapq.heappop(heap)         
            
            # update smallest_range
            if max_val - min_val < smallest_range[1] - smallest_range[0]:  
                smallest_range = min_val, max_val
                
            # if list is exhausted, return the range
            if num_index + 1 == len(nums[list_index]):                   
                return smallest_range
            
            # get the next element from the list that has the current min value
            next_num = nums[list_index][num_index+1]                     
            max_val = max(max_val, next_num)
            heapq.heappush(heap, (next_num, list_index, num_index+1))
