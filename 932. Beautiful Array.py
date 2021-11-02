class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        """
        Divide and Conquer
        there is no k with A[k] * 2 = odd + even
        n = 5: [1, 5, 3, 2, 4]
        beautiful = beautiful of odds + beautiful of evens
        *2 or +- to beatiful array -> still beatiful -> we can make beautiful array all odd/even
        
        Recursion: Time O(nlogn)
        Iterative: Time O(n)
        
        """
        def find_beatiful_of_length(n):
            if n == 1: 
                return [1]
            l = find_beatiful_of_length(n//2 + n%2) # add n%2 to have n elements in total
            r = find_beatiful_of_length(n//2)
            # beautiful of odds + beautiful of evens
            return [x*2-1 for x in l] + [x*2 for x in r]
        
        return find_beatiful_of_length(n)
    
        # res = [1]
        # while len(res) < n:
        #     # beautiful of odds + beautiful of evens
        #     res = [x * 2 - 1 for x in res] + [x * 2 for x in res]
        # return [x for x in res if x <= n]
