class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        # Mono stack
        
        # result = sum{ Max(subarray) - Min(subarray) } 
        #        = sum{Max(subarray)} - sum{Min(subarray)}
        #        = sum_max - sum_min
        
        # sum_min = sum(range_where_nums[i]_is_smallest * nums[i])
        # range = (i - index of the previous smaller value) * (index of the next smaller value - i)
        
        # Time O(n)
        # Space O(n)
        
        n = len(nums)
        sum_min = sum_max = 0
        
        stack = []
        for next_smaller in range(n + 1):
            while stack and (next_smaller == n or nums[next_smaller] < nums[stack[-1]]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                sum_min += nums[i] * (next_smaller - i) * (i - prev_smaller)
            stack.append(next_smaller)
            
        stack = []
        for next_larger in range(n + 1):
            while stack and (next_larger == n or nums[next_larger] > nums[stack[-1]]):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                sum_max += nums[i] * (next_larger - i) * (i - prev_larger)
            stack.append(next_larger)
        
        return sum_max - sum_min
