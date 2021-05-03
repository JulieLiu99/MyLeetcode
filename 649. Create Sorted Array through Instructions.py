class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        '''
        # This is slow
        # bisect.insort() is O(N)
        # So in total O(N^2), instead of O(NlogN)
        
        nums = []
        
        ans = 0
        
        for ins in instructions:
            index1 = bisect.bisect_left(nums, ins)
            left = index1
            
            index2 = bisect.bisect_right(nums, ins)
            right = len(nums) - index2
            
            ans += min(left, right)
            bisect.insort(nums, ins) # inserting ins in nums after any existing entries of ins
        
        mod = 10**9+7
        
        return ans % mod
        '''
        
        # Binary Index Tree
        #
        # update O(logn)
        # addSum O(logn)
        # Time O(NlogM),
        # Space O(M)
        # where M is the range of instructions[i]
        
        M = max(instructions)
        
        tree = [0] * (M+1)
        
        def update(i, k):
            while i <= M:
                tree[i] += k
                i += i & -i
        
        def getSum(i):
            ans = 0
            while i > 0:
                ans += tree[i]
                i -= i & -i
            
            return ans
        
        ans = 0
        
        for i, num in enumerate(instructions):
            left = getSum(num-1)
            right = i - getSum(num)
            ans += min(left, right)
            update(num, 1)
        
        mod = 10**9+7
        
        return ans % mod
