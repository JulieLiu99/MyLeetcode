class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Twp Pointers
        
        Time O(n): two pointers go through string once, reverse O(substring)
        Space O(1): with reverse substring becomes O(n), could be reduced to O(1)
        
        """
        delete = 0
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
                """
                delete += 1
                if delete > 1:
                    return False

                # skip one of the two
                # this doen't work because in this case
                # lcupuu...uupucul
                #  ^            ^
                # both l += 1 and r -= 1 create matches
                # but only one is correct
                
                if s[l+1] == s[r]:
                    l += 1
                elif s[l] == s[r-1]:
                    r -= 1
                else:
                    return False
                """
        return True
