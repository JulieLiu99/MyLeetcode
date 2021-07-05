class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Recursion
        
        Time O(nk)
        Space O(nk)
        
        """
        
        nums = [_ for _ in range(1, n+1)]   # [1, n]
        res = []
            
        # i: next pick starts from index i
        # path: all picked numbers up till now
        def find(i, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(i, n): 
                find(i+1, path + [nums[i]])
                
        find(0, [])
        return res
        
