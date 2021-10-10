class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Deque
        
        Time O(n)
        Space O(k)
        
        """
        n = len(nums)
        q = deque([])  # store index of `nums` elements, elements is in decreasing order, the front is the maximum element.
        res = []
        for i in range(n):
            # Remove out of range element
            if q and q[0] <= i - k: q.popleft()
                
            # Remove elements less or equal to nums[i]
            while q and nums[q[-1]] <= nums[i]: q.pop()  
                
            # Push index of current nums[i] to the deque
            q.append(i)
            
            # if window reaches size k -> add result
            if i + 1 >= k: res.append(nums[q[0]])
                
        return res
