class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_bits(self, num):
        bit_num = bin(num)[2:].zfill(32) # 0b...
        node = self.root
        for bit in bit_num:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    
    def find_max_xor(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        max_xor = ''
        for bit in bit_num:
            if bit == '0':
                oppo_bit = '1'
            elif bit == '1':
                oppo_bit = '0'
            
            if oppo_bit in node.children:
                max_xor += oppo_bit
                node = node.children[oppo_bit]
            else:
                max_xor += bit
                node = node.children[bit]
        
        return int(max_xor, 2) ^ num
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=wSgrc98d2lI
        Time O(N) traverse once, where N is length of num in binary
        Space O(N K) need to store all nums in trie, where K is length of nums
        """
        for num in nums:
            self.insert_bits(num)
        
        max_ = 0
        for num in nums:
            max_ = max(max_, self.find_max_xor(num))
            
        return max_
