class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        Solution 1: Brute Force (TLE)

        Brute force all combinations, will TLE.
        Time O(N^4)
        Space O(1)
        
        """

        """
        Solution 2: Brute Force with prefix

        Calculate all prefix of bitwise-xor operation.
        prefix[0] = 0
        prefix[i] = A[0]^A[1]^...^A[i - 1]
        So that for each (i, j),
        we can get A[i]^A[i+1]^...^A[j] by prefix[j+1]^prefix[i]
        in O(1) time

        Time O(N^3)
        Space O(N)
        
        """
        
#         n = len(arr)
#         prefix = [0] # prefix[1] = 0 ^ arr[0] = arr[0]
        
#         for i in range(n):
#             prefix.append(prefix[i] ^ arr[i])
            
#         res = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j, n):
#                     if prefix[j]^prefix[i] == prefix[k+1]^prefix[j]:
#                         res += 1 
#         return res

    
        """
        Solution 3: Prefix XOR

        a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

        Assume a == b, thus
        a ^ a = b ^ a, thus
        0 = b ^ a, thus
        arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
        prefix[k+1] = prefix[i]

        We only need to find out how many pair (i, k) of prefix value are equal.
        So we can calculate the prefix array first,
        then brute force count the pair.

        Because we once we determine the pair (i,k),
        j can be any number that i < j <= k,
        so we need to plus k - i to the result res.

        Time O(N^2)
        Space O(N)
        
        """
        
    
        n = len(arr)
        prefix = [0] # prefix[1] = 0 ^ arr[0] = arr[0]
        
        for i in range(n):
            prefix.append(prefix[i] ^ arr[i])
            
        res = 0
        for i in range(n):
            for k in range(i, n):
                if prefix[i] == prefix[k + 1]:
                    res += k - i 
                    
        return res