class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        First turn the input into a set of numbers to get rid of repetition and for faster retrieval. 
        That takes O(n) and then we can ask in O(1) whether we have a certain number.

        Then go through the numbers.
        Skip if num is not the start a sequence (i.e., num-1 is in the set).
        If num is the start of a sequence, look for num+1 until it is not in the set anymore. 
        The length of the sequence is num - start + 1 and we update res with that. 
        Since we check each sequence only once, this is overall O(n). 
        
        Time O(n)
        Space O(n)
        
        """
        
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in nums: # start of a sequence
                start = num
                while num + 1 in nums:
                    num += 1
                res = max(res, num - start + 1)
        
        return res
