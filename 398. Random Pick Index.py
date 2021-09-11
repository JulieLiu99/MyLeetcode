class Solution:

    """
    Reservoir Sampling
    
    E.g.

    0 1 2 (indices)
    3 3 3 (values)

    step 1: select the first sample "3" (index 0), the probability to select this sample is 1/1 and the probability that this selected item will remain in the reservior is 1/3 (other 2 samples could replace it), setting the resulting probablity to 1/1 * 1/3 -> 1/3

    step 2: select out of the first two samples "3" (index 0, index 1), the probability to select the second sample is 1/2 and the probability that it will remain in the reservior is 2/3 (other 1 sample could replace it), setting the resulting probablity to 1/2 * 2/3 -> 1/3

    step 3: select out of the first three samples "3" (index 0, index 1, index 2), the probability to select the third sample is 1/3 and the probability that it will remain in the reservior is 3/3 or simply 1.0 (none other samples could replace it), setting the resulting probablity to 1/3 * 1 -> 1/3
    
    """
#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def pick(self, target: int) -> int:
#         cnt = 0
#         for idx, num in enumerate(self.nums):
#             if num == target:
#                 cnt += 1
#                 prob = 1 / (cnt)
#                 if random.random() < prob:
#                     selected = idx
#         return selected

    def __init__(self, nums: List[int]):
        self.nums = nums
		
    def pick(self, target: int) -> int:
        cnt = 0
        selected = 0
        
        for idx, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randint(1, cnt) == 1: # random.randint(start, stop) = randrange(start, stop+1)
                    selected = idx
        return selected

    """
    Random Choice
    
    """

#     def __init__(self, nums: List[int]):
#             self.nums = nums

#         def pick(self, target: int) -> int:
#             answer = []
#             for idx, num in enumerate(self.nums):
#                 if target == num:
#                     answer.append(idx)
#             return random.choice(answer)

    """
    Dictionary to store indexes first
    
    """
#     def __init__(self, nums: List[int]):
#         self.val_idx = collections.defaultdict(list)
#         for i, num in enumerate(nums):
#             self.val_idx[num].append(i)

#     def pick(self, target: int) -> int:
#         idxes = self.val_idx[target]
#         return random.choice(idxes)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)