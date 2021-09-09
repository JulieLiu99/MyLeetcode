class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Set store visited
        
        Time O(n)
        Space O(n) -> NO
        
        """
        """
        Sort and then compare if there are consequtive duplicates 
        
        Time O(nlogn)
        Space O(n) -> NO
        
        """
        
        """
        Modify in place -> NO
        And store visited by index = abs(num)
        
        Because 1 <= nums[i] <= n
        Whenevr visit a num for the first time, flip nums[abs(nums[i])] to negative
        Next time if encounter duplicate, nums[abs(nums[i_duplicate])] will be negative
        
        Time O(n)
        Space O(1)
        
        """
        # for i in range(len(nums)):
        #     index = abs(nums[i])
        #     if nums[index] < 0:
        #         return index
        #     nums[index] *= -1
        
        """
        Linked List Cycle + Floyd Algorithm
        
        Linked List Cycle:
        num = idx -> nums[idx] -> nums[nums[idx]]
        Duplicate nums[index] gets pointed to twice -> start of a cycle
        0 is never pointed at (1 <= nums[i] <= n), nums[0] is start
        
        Floyd Algorithm
        
        1 is the duplicate -> find it with two pointers, slow and fast (2*slow)
        let's say circle has length C, 
        P is length from start 0 to duplicate 1, 
        and X is distance from first meeting point of slow and fast
        2 * (P + C - X) = P + C + C - X
                      P = X
          P
        0 -> 1 -> 2 -> 3
              ^        |
             X \       V
                \ 5 <- 4
                
        step1: slow pointer moves one step, fast pointer moves two steps
        step2: slow pointer meet fast pointer, reset slow pointer and slow down fast pointer
        step3: slow pointer meet fast pointer at duplicate num
        
        Time (n)
        Space (1)
        
        """
        slow = 0
        fast = 0
        step1 = 1
        step2 = 2
        
        while True:
            
            slow = nums[slow]
            for i in range(step2):
                fast = nums[fast]
                
            if slow == fast:
                if step2 == 2: # first meetup
                    slow = 0
                    step2 = 1
                else:           # second meetup
                    return slow
