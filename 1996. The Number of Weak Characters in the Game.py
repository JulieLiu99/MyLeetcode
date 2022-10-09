class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Sort + Greedy
        
        sort attack big to small: new item's attack <= previous ones
        sort defence small to big: whenever new item's defence < previous max, it's beaten!
        
        Q: how do we know a weak item's attack is strictly smaller?
        A: if = instead of <, e.g. [1,2], [1,3], [1,5], nothing will be beaten because defence is in increasing order!
        """
        properties.sort(key=lambda x: (-x[0], x[1])) 
        
        res = 0
        cur_max = 0
        
        for _, defence in properties:
            if defence < cur_max:
                res += 1
            else:
                cur_max = defence
        return res
