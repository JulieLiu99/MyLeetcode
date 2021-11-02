class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Heap sort
        
        Time O(nlogn)
        Space O(n)
        
        """
        if not S:
            return ""
       
        d = collections.Counter(s)

        heap = []
        for char, count in d.items():
            heappush(heap, (-count, char))

        res = ""
        while len(heap) >= 2: # at least 2 different chars     
            count1, char1 = heappop(heap)
            count2, char2 = heappop(heap)

            res += char1 + char2

            if abs(count1) > 1: # if more of char, push back with count-1
                heappush(heap, (count1+1, char1))

            if abs(count2) > 1: 
                heappush(heap, (count2+1, char2)) 


        if heap: # check last char
            count, char = heap[0]
            if abs(count) > 1: # repeated same char, failure
                return "" 
            else:
                res += char
        return res
