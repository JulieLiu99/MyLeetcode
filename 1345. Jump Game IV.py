class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        BFS until last index is reached
        
        1. Use a defaultdict, where for each value we keep list of all possible indexes for this value
        
        2. Use a set of visited nodes, we need it in usual bfs, not to visit any node two times.
        
        [
        del valueToIndexes[arr[node]]:
        Imagine, we have arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]. The first time we see 1, we visit all other 1s. Second time we see 1, we do not need to visit its neighbors of same value. Without this optimization time complexity could be O(n^2).
        ]
        
        3. Do classical bfs: Extract node from queue, visit left and right neighbors, and visit all of its same value neighbors if not yet.
        
        Time O(N)
        Space O(N)
        
        Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
        
        """
        n = len(arr)
        valueToIndexes = defaultdict(list)
        
        for i, num in enumerate(arr):
            valueToIndexes[num].append(i)
            
        queue = collections.deque([0])
        seen = set()
        seen.add(0)
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                nxt = []
                
                if node == n-1: # if reach last index
                    return steps
                
                if node > 0:
                    nxt.append(node-1)
                if node < n-1:
                    nxt.append(node+1)
                if arr[node] in valueToIndexes:
                    nxt.extend(valueToIndexes[arr[node]])
                    del valueToIndexes[arr[node]] # so that it won't be appended to queue again
                    
                for neighbor in nxt:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
                    
            steps += 1
