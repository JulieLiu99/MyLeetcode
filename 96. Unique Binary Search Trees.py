class Solution:
    """
    DP, Bottom Up

                   left         right
    numTree[4] = numTree[0] * numTree[3] +
                 numTree[1] * numTree[2] + 
                 numTree[2] * numTree[1] +
                 numTree[3] * numTree[0]

    Time O(n^2): for each numTree[i], go through exising numTree[<i]
    Space O(n)

    """
#     def numTrees(self, n: int) -> int:
    
#         numTree = [1 for _ in range(n+1)]
        
#         # 0 node = 1 tree
#         # 1 node = 1 tree
#         for tree_size in range(2, n+1):
#             total = 0
#             for root in range(1, tree_size+1):
#                 left = root -1
#                 right = tree_size - root
#                 total += numTree[left] * numTree[right]
#             numTree[tree_size] = total
            
#         return numTree[n]

    """
    DP, Top Down

    Time O(n^2)
    Space O(n^2)

    """
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        
        if n == 0: return 1
        
        res = 0
        
        for i in range(1, n+1):
            res += self.numTrees(i-1) * self.numTrees(n-i)
            
        return res
