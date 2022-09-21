class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        Step 1: For every update with startIdx, endIdx, and incrementValue:
        res[startIdx] += incrementValue
        res[endIdx + 1] -= incrementValue (if endIdx + 1 is out of range, don't need to do anything)
        
        Step 2: At the end, traverse the array and set: res[i] += res[i-1]. This is basically prefix-sum.
        
        Time O(N + K)
        Space O(N)
        
        """
        res = [0] * length
        for start, end, value in updates:
            res[start] += value
            if end + 1 < length:
                res[end + 1] -= value

        for i in range(1, length):
            res[i] += res[i-1]

        return res
