class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        """
        Start with i = j = k, score = nums[k].
        While incrementing the size of window,
        reduce min(nums[i]...nums[j]) slowly.

        To do so, check values on both sides of the window.
        If nums[i - 1] < nums[j + 1], we do j = j + 1
        If nums[i - 1] >= nums[j + 1], we do i = i - 1

        Time O(n)
        Space O(1)

        """
        
        score = mini = nums[k]
        i, j, n = k, k, len(nums)
        
        while i > 0 or j < n - 1:
            
            if i == 0:
                j += 1
            elif j == n-1:
                i -= 1
            elif nums[j + 1] > nums[i - 1] :
                j += 1
            else:
                i -= 1
                
            mini = min(mini, nums[i], nums[j])
            score = max(score, mini * (j - i + 1))
            
        return score
    
