class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        """
        Time O(N)
        Space O(1)
        
        """
        
        p = preorder.split(',')
        
        # one empty slot for the root
        slot = 1
        for node in p:
            
            # no empty slot to put the current node
            if slot == 0:
                return False
                
            # a null node?
            if node == '#':
                # a null node occupies one slot
                slot -= 1
            else:
                # a non-null node takes one slot (-1) and creates two more (+2)
                slot += 1
        
        # all slots must be taken
        return slot==0
