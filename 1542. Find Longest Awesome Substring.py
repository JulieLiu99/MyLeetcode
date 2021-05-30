class Solution:
    def longestAwesome(self, s: str) -> int:
        
        """
        Solution 0: Brute Force
        Keep track of all counters while looping through characters. Once at position i, go back and subtract all previous counters from current counter to check if any of them is awesome. 
        O(n^2), TLE
        
        Solution 1: Prefix + Hashtable
        
        Define a state of prefix string input [0~i]
        Update the state when extend the prefix
        state_idx[state] = first/last index when state occurred
        
        Assume satte s_i, s_j occurred at [i, j], i<j, cond(s_i, s_j) == True,
        input[i+1 ~ j] is a solution and its length is j - (i + 1) + 1 = j - i.
        
        state_idx[s_init] = -1 # base state "occurred" before the start.
        --> handles the case when the entire prefix is a solution
        
        ans = max/min(i - state_idx[s_cur]), o <= i < n
        
        There are 2 cases that a string can be reordered to be a palindrome:
        Case 1. All of its characters have even occurrences:
                "2424" -> there are two '2's and two '4's.
        Case 2. All of its characters have even occurrences except one:
                "24241" -> there are two '2's, two '4's and one '1'
                Flip an arbirary bit to make that digit occur "even" times.
                New state = state ^ (1 << d)

        BitMask 
        Use one bit to represent if the digit has even or odd count.
        Let 0 represent "even" and 1 represent "odd".

        Time O(10*n)
        Space O(|states|) = O(2^10) = O(1)

        """
        
        n = len(s)
        ans, mask = 0, 0
        
        state_idx = [n] * 1024
        state_idx[0] = -1
        
        for i in range(n):
            mask ^= 1 << int(s[i])
			
			# Check for Case 1, all even counts
            ans = max(ans, i - state_idx[mask])
            
			# Check for Case 2, only one bit odd count
            for j in range(10):
                test_mask = mask ^ (1 << j)
                ans = max(ans, i - state_idx[test_mask])
                
			# save the earliest position
            state_idx[mask] = min(state_idx[mask], i)    
        
        return ans
