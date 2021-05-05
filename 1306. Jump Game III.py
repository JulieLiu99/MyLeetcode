class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Recursion DFS
        
        Time O(N), as each number will be flipped at most once.
        Space O(N) for recursion.
        
        """
        
        if 0 <= start < len(arr) and arr[start] >= 0: 
            
            arr[start] = -arr[start] # mark as visited
            
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        
        return False
    
    
        """
        # same as this:
        
        def DFS(pos)
            if 0 <= pos < len(arr) and arr[pos] < len(arr) and pos not in seen:
                seen.add(pos)
                return arr[pos] == 0 or DFS(pos + arr[pos]) or DFS(pos - arr[pos])
            return False
    
        seen = set()
        return DFS(start)
        """
