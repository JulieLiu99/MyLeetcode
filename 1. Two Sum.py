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
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
