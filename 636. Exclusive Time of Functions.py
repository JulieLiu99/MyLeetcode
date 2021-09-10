class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        "{function_id}:{"start" | "end"}:{timestamp}"
        
        Stack
        
        Current executing function is on top
        If new function comes: current function pause, new function comes to top 
        If current function ends: remove it from stack, let function below execute if any
        
        Time O(n)
        Space O(n)
        
        """
        res = [0] * n
        stack = []
        
        for log in logs:
            f_id, state, timestamp = log.split(":")
            f_id, timestamp = int(f_id), int(timestamp)

            if state == "start":
                if stack: # a function has been executing -> needs to pause now
                    res[stack[-1]] += timestamp - previous_timestamp
                stack.append(f_id) # new function comes to top and starts executing
                
            else: # end
                # remove current function from stack
                # +1 because function ends at the end of unit time
                timestamp += 1
                res[stack[-1]] += timestamp - previous_timestamp 
                stack.pop()
                
            previous_timestamp = timestamp
        
        return res
