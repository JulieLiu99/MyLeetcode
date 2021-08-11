class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        Two Pass
        Create a clean string first
        Then two pointers loop through clean string
        
        Time O(n)
        Space O(n)
        
        """
        
        new_s = ""
        for c in s:
            if c.isalnum(): 
                new_s += c.lower()
        
        l = 0
        r = len(new_s) - 1
        
        while l<r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True

    
        """
        One Pass
        No clean string
        Two pointers loop through original string
        If invalid char, skip it
        
        Time O(n)
        Space O(1)
        
        Surprisingly, it's actually a bit slower than prev solution in practice
        
        """
    
#         l = 0
#         r = len(s) - 1
        
#         while l < r:
#             while not s[l].isalnum() and l < r:
#                 l += 1
            
#             while not s[r].isalnum() and l < r:
#                 r -= 1
                            
#             if s[l].lower() == s[r].lower():
#                 l += 1
#                 r -= 1
#             else:
#                 return False
        

#         return True


