class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums: List[int]
        target: int
        return: List[int]
        
        Time complexity O(n): traverse list once. each look up in the hash table costs O(1)
        Space complexity O(n): the exptra space required depends on the number of items stored in the hash table, at most n elements
        
        """
        hashmap = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[num] = index
        return None
