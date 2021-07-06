"""
Brute Force

Travers nums[left:right+1]

sumRange:
Time O(n)
Space O(n)

Works but slow

"""

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         s = 0
#         for i in range(left, right+1):
#             s += self.nums[i]
            
#         return s

"""
Because a lot of calls will be made to sumRange
Use Presum

sumRange:
Time O(1)
Space O(n)

"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]    # presum[i] = nums[0] + ... + nums[i-1]
                             # presum[1] = nums[0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
