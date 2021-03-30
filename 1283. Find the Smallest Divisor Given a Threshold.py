class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        """
        Binary search
        
        Time O(log(max(nums) * n)
        Space O(1)
        
        """
        
        def isOK(divisor):
            sum = 0
            for num in nums:
                sum += math.ceil(num/divisor)
            if sum <= threshold:
                return True
            return False

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if isOK(mid):
                right = mid
            else:
                left = mid + 1
        return left
