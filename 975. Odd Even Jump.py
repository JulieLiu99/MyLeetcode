class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
#         Approach 1: Brute Force
#         Simulate teh deterministic jumping process, each element O(n) time
        
#         Time O(n^2) in total
#         Time Limit Exceeded


#         Approach 2: DP + Binary Search
        
#         Odd jump (up): find the smallest value >= than self
#         Even jump (down): find the largets value <= than self
            
#         map<int, int> --> min index of a value
#         higher[i] True means can reach end from i starting with a up jump
#         lower[i] True means can reach end from i starting with a down jump
        
#         Start from the (n-2)th element because n-1 is True, True
#         Find a valid up jump index j 
#         Find a valid down jump index k
        
#         higher[i] = lower[j]     next jump will be even/down
#         lower[i] = higher[k]     next jump will be odd/up
        
#         ans = sum(higher)
#         Time O(nlogn): for each element, find up/down jump each O(logn)
#         Space O(n): DP arrays higher and lower
        
    
#         In Python, use stack to find next_higher and next_lower

        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        
        stack = []
        for v, i in sorted([v, i] for i, v in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for v, i in sorted([-v, i] for i, v in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n-1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
            
        return sum(higher)
        
