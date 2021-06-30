class Solution:
    def simplifyPath(self, path: str) -> str:
        
        """
        While loop, update path inplace
        
        Pass but slow
        Time O(n)
        Space O(1)
        
        """
        
#         i = 0
#         while i < len(path):
            
#             # "///" -> "/"
#             if path[i] == "/":
#                 slash_start = i - 1
#                 i += 1
#                 while i<len(path) and path[i] == "/":
#                     i += 1
#                 while slash_start>=0 and path[slash_start] == "/":
#                     slash_start -= 1
#                 # i is first index not "/"
#                 # slash_start is last index not "/"
#                 path = path[:slash_start+1] + "/" + path[i:]
#                 i = slash_start+2
                
#             # "." or ".." -> ""
#             elif path[i] == ".":
#                 count = 0
#                 j = i
#                 while j<len(path) and path[j] == ".":
#                     count += 1
#                     j += 1
#                 if count == 2 and path[i-1] == "/" and (i+2 > len(path)-1 or path[i+2] == "/"):
#                     slash = i-2 # previous directory last index
#                     while slash>0 and path[slash] != "/":
#                         slash -= 1
#                     # slash is index of slash after upper directory
#                     if slash >= 0:  # /a/../b -> /b
#                         path = path[:slash] + path[i+count:]  
#                         i = slash
#                     else:           # /../ -> /
#                         path = path[i+count:]  
#                         i = 0
#                 elif count == 1 and path[i-1] == "/" and (i+1 > len(path)-1 or path[i+1] == "/"):
#                     path = path[:i-1] + path[i+1:]  
#                 else: 
#                     i += count
            
#             else:
#                 i += 1

#         # hand extra "/" at the end
#         if len(path) > 1 and path[-1] == "/":
#             return path[:-1]
#         # "/." -> "" -> "/"
#         elif len(path) == 0:
#             return "/"
#         return path
                    
        """
        Stack
        
        path.split("/"):
        "/a/./b/../../c/" -> ['', 'a', '.', 'b', '..', '..', 'c', '']
        
        """
        parts = path.split("/")
        stack = []
        for part in parts:
            if part in ['', '.']:
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
