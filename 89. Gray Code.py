class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        """
        Reuse Gray Code from previous n

        Mirror the existing gray code sequence

        Add all 0's to the first half   -> preserve gray code quality among them
        Add all 1's to the second half  -> preserve gray code quality among them

        For each gray code pairs, resulted from mirroring:
        -> one has 0 in front, the other has 1 in front 
        -> gray code quality created

        e.g.
        n = 1       n = 2

        0   ->    0  ->  00
        1         1  ->  01
            ->    1  ->  11
                  0  ->  10

        Time O(2^n): for each n, double the result list
        Space O(2^n)
        
        """
        if n == 0:
            return [0]

        res = [0,1]

        # when n = 2 ... n: mirror + append 0/1
        for i in range(2, n+1): 
            # only need to append 1 to the front
            # because appending 0 to the front requires no change to vals
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] | 1<<i-1)

        return res
