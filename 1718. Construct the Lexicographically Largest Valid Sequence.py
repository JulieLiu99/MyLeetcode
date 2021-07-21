class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Backtrack, DFS Recursion
        
        Greedily fill each position with the largest possible value.
        Need to reverse self.res[] and seen() if current backtracking is unsuccessiful.
        
        Time O(n!)
        Space O(n!)
        
        """
        
        seen = set()
        size = 1 + (n-1) * 2
        
        self.res = [0 for _ in range(size)]
        
        def dfs(i):
            
            if i == size:
                return True
            
            if self.res[i] != 0: # filled already
                return dfs(i+1)
            else:
                for num in range(n, 0, -1): # try large ones first
                    if num not in seen:
                        if num == 1:
                            self.res[i] = 1
                            seen.add(num)

                            if dfs(i+1):
                                return True

                            self.res[i] = 0
                            seen.remove(num)

                        elif i + num < size and self.res[i+num] == 0:
                            self.res[i] = self.res[i+num] = num
                            seen.add(num)

                            if dfs(i+1):
                                return True

                            self.res[i] = self.res[i+num] = 0
                            seen.remove(num)
                            
                return False
            
        dfs(0)
        
        return self.res
