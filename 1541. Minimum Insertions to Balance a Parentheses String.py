class Solution:
    def minInsertions(self, s: str) -> int:
        
        """
        
        res represents the number of left/right parentheses already added.
        right represents the number of right parentheses needed.

        1) case )
        If we meet a right parentheses , right--.
        If right < 0, we need to add a left parentheses before it.
        Then we update right += 2 and res++
        This part is easy and normal.

        2) case (
        If we meet a left parentheses,
        we check if we have odd number ')' before.
        If we have odd ')' before, we want right parentheses in paires.
        So add one ')' here, then update right--; res++;.
        Note that this part is not necessary if two consecutive right parenthesis not required.
        Because we have (, we update right += 2.
        
        
        E.g. ((()(
        i=0, we have ( it means we need two right parenthesis (they are in pair) so.. right+=2 => res =0, right =2
        i=1, again we have ( it means we need two right parenthesis (they are in pair) so.. right+=2 => res =0, right =4
        i=2, again we have ( it means we need two right parenthesis (they are in pair) so.. right+=2 => res =0, right =6
        i=3, we have ) we subtract one from right. so.. right-- => res =0, right =5
        i=4, we have ( but here right is odd so we need to make it even with right-- and increment res++ => res =1, right =4. Also, as we have got a left parenthesis then we need two right parenthesis (they are in pair) so.. right+=2 => res =1, right =6

        finally ans is res + right => 1 + 6 == 7


        Time O(N)
        Space O(1)
        
        """
        
        res = right = 0
        
        for c in s:
            
            if c == '(':
                if right % 2:   # odd ) before this, add one ) 
                    right -= 1
                    res += 1
                right += 2      
                
            if c == ')':
                right -= 1
                if right < 0:   # ) is extra, add ( before this
                    right += 2
                    res += 1
                    
        return right + res
