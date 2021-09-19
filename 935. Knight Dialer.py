class Solution:
    def knightDialer(self, n: int) -> int:
        """
        DP
        
        two squares vertically and one square horizontally, 
        or two squares horizontally and one square vertically
        x, y in [(-1, 2), (-1, -2), (1, 2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
        
        Given an integer n, return how many distinct phone numbers of length n we can dial.
        perform n - 1 jumps to dial a number of length n
        
        dp[button] stores the current number of ways to reach button (1~0)
        prev[botton] stores the number of ways to reach button (1~0) in previous round
        
        In the end prev is the last dp, so return sum(prev) % (10**9 + 7)
        
        Time O(n * 10)
        Space O(10)
        
        """
        prev_buttons = {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6 :[0,1,7],
            7 :[2,6],
            8 :[1,3],
            9 :[2,4],
            0: [4,6]
        }

        prev = [1 for _ in range(10)] # for length 1, each botton has 1 way to be reached (place the knight there initially!!)
        dq = [0 for _ in range(10)]
        
        for length in range(2, n+1): # for length 2 to n
            
            for button in range(10): 
                
                for prev_button in prev_buttons[button]:
                    dq[button] += prev[prev_button] % (10**9 + 7)
                    
            prev = dq 
            dq = [0 for _ in range(10)]
        
        return sum(prev) % (10**9 + 7)
