class Solution:
    def isPalindrome(self, x: int) -> bool:

        """
        Get the len and check left and right 
        
        Time O(log_10(n))
        Space O(1)
        
        """
        if x < 0:
            return False
        
        ls = len(str(x))

        for i in range(int(ls/2)):
            
            temp_right = int(x / (10 ** i))
            right = temp_right % 10   # the right side digit
            temp_left = int(x / (10 ** (ls-i-1)))   
            left = temp_left % 10      # the left side digit
            
            if left != right:
                return False
            
        return True
