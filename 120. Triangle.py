class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        """
        Recursion
        
        TLE, even with @lru_cache(None)
        
        Time O(rows^2)
        Space O(rows^2)
        
        """
        
#         rows = len(triangle)
        
#         @lru_cache(None)
#         def dfs(row, i, path_sum):
#             if row == rows - 1:
#                 if i+1 < len(triangle[row]):
#                     return path_sum + min(triangle[row][i], triangle[row][i+1])
#                 else:
#                     return path_sum + triangle[row][i]
                
#             if i+1 < len(triangle[row]):
#                 return min(dfs(row+1, i, path_sum+triangle[row][i]), dfs(row+1, i+1, path_sum+triangle[row][i+1]))
#             else:
#                 return dfs(row+1, i, path_sum+triangle[row][i])
                
#         return dfs(0,0,0)

        """
        Bottom Up DP
        
        res[i] = the min sum from bottom till current row, with triangle[row][i] in the path
        
        Time O(rows)
        Space O(rows)
        """

        rows = len(triangle)
        res = [0] * (rows + 1)
        for row in range(rows-1, -1, -1):
            for i in range(len(triangle[row])):
                # update res, by adding triangle[row][i] and the smaller path from previous rows
                res[i] = triangle[row][i] + min(res[i], res[i + 1])
                
        return res[0]
