class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Stack
        
        If check current against stack[-1] till stack[-k+1], remove if they all equal
        k = 3, check stack[-1] and stack[-2]
        Else append
        
        If not k-1 elements in stack yet, append
        
        Return ''.join(stack)
        
        Time O(n): technically O(nk) because each check takes O(k)
        Space O(n)
        
        """
#         stack = []
            
#         for i in range(len(s)):
            
#             if len(stack) < k-1:  # not enough (k-1) elements in stack, append
#                 stack.append(s[i])
                
#             else:                 # check if (k-1) top elements + s[i] is duplicate
#                 duplicate = True
#                 for j in range(-k+1, 0): 
#                     if stack[j] != s[i]:
#                         duplicate = False
#                         break
#                 if duplicate:
#                     for j in range(-k+1, 0):
#                         stack.pop()
#                 else:
#                     stack.append(s[i])
            
#         return ''.join(stack)
                
    
        """
        Optimization: [element, count] in stack
        
        Instead of storing individual elements
        Also store their consecutive counts
        
        Time O(n)
        Space O(n)
        
        """
        stack = [] # [val, count]
        
        for val in s:
            
            if stack and stack[-1][0] == val:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([val, 1])
            
        output = ''
        for val, count in stack:
            output += val * count
            
        return output
        
