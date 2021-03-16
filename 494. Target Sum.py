class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        """
        Use a dictionary to store all possible sums using all the numbers with +/- signs
        Return the number of ways of the target sum in the dictionary
        
        Time O(2 ^ len(nums))
        Space O(2 ^ len(nums))
        
        """

        counter = {0: 1}
        
        for num in nums:
            tmp = {}
            for val, count in counter.items():
                s = val + num
                tmp[s] = tmp.get(s, 0) + count

                s = val - num
                tmp[s] = tmp.get(s, 0) + count
            counter = tmp

        return counter.get(S, 0) 
        # get() returns value for the given key ( if key not available, returns default value)
        
        
        """
        # Recursion 
        # Time O(2^len(nums))
        # Space O(len(nums) * sum) 
        
        def df(amount, index):
            if (amount, index) in map:
                return map[(amount, index)]
            if index == len(nums):
                if amount == 0:
                    return 1
                else:
                    return 0
            map[(amount, index)] = df(amount - nums[index], index+1) + df(amount + nums[index], index+1)
            return map[(amount, index)]
        
        map = {}
        return df(S, 0)
    
        """
