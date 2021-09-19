class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        Two Pointers
        
        If two elements in two arrays are of same length, record their common frequency, move forward in both arrays
        If on element has more frequency, record their common frequency, update the larger frequency (minus the smaller one), move forwared in smaller arry
        
        Value to be appended is ele1 * ele2
        If value is same as previous value, merge the two frequencies
        
        Time O(n)
        Space O(1)
        
        """
        i = j = 0
        res = []
        
        while i < len(encoded1) and j < len(encoded2):
        
            val = encoded1[i][0] * encoded2[j][0]
            
            l1 = encoded1[i][1]
            l2 = encoded2[j][1]
            
            if l1 == l2: 
                freq = l1
                i += 1
                j += 1
                
            elif l1 < l2: # move to next element in encoded1 & update freq for unprocessed encoded2
                freq = l1
                i += 1
                encoded2[j][1] = l2-l1 
                
            else: # l1 > l2 # move to next element in encoded2 & update freq for unprocessed encoded1
                freq = l2
                j += 1
                encoded1[i][1] = l1-l2 
            
            if res and res[-1][0] == val: # merge if val == previous val
                res[-1][1] += freq
        
            else:
                res.append([val, freq])
                
        return res
