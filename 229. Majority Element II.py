class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Simple brute force
        
        Time O(n)
        Space O(n)
        
        """
        
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        return [key for key in count.keys() if count[key] > len(nums)//3]
        
    
        """
        Slight space optimization
        
        Ff an element appears more than n//3 times,
        then it still exists after being removed n//3 times.
        
        Time O(n)
        Space O(3)
        
        """
        
        # ctr = collections.Counter()
        # for num in nums:
        #     ctr[num] += 1
        #     if len(ctr) == 3:
        #         ctr -= collections.Counter(set(ctr))
        # return [num for num in ctr if nums.count(num) > len(nums)//3]
