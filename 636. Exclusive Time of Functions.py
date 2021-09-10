class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Stack
        
        "{function_id}:{"start" | "end"}:{timestamp}"
        
        Time O(n)
        Space O(n)
        
        """
        res = [0] * n
        stack = []
        
        for log in logs:
            f_id, state, timestamp = log.split(":")
            f_id, timestamp = int(f_id), int(timestamp)
            
            if stack: # a function has been executing -> needs to pause/end now
                res[stack[-1]] += timestamp - previous_timestamp
            
            if state == "start":
                stack.append(f_id) # new function comes to top and starts executing
            else: # end
                # remove current function from stack
                # +1 because function ends at the end of unit time
                res[stack.pop()] += 1 
                timestamp += 1

            previous_timestamp = timestamp
        
        return res
