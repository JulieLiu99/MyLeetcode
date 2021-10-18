# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """
        Stack 
        
        Frist num is root, in the stack
        if (, store previous value in a node and push to stack
        If ), go up, pop one node and attach it to parent (stack[-1]) -> left first, then right
        
        "4(2((3)1))(6(5))"
        
        4( 
        [4]  
        
        4(2(
        [4, 2]
        
        4(2((3)         4
        [4, 2]       
                      2
                     /
                    3
                     
        4(2((3)1)        4
        [4]       
                       2
                      / \
                     3   1
                     
        4(2((3)1))       4
        [4]             /
                       2
                      / \
                     3   1
        
        Time O(n)
        Space O(n)        
        
        """
        if not s: 
            return None 
        
        stack = []
        val = ""
        for ch in s: 
            if ch == "(": # end of parent
                if val: 
                    node = TreeNode(int(val))
                    stack.append(node)
                    val = ""
                    
            elif ch == ")": 
                if val:  # end of new node 
                    node = TreeNode(int(val))
                    val = ""
                else:    # end of subtree
                    node = stack.pop()
                    
                if stack[-1].left is None: 
                    stack[-1].left = node 
                else: 
                    stack[-1].right = node
                    
            else: val += ch
                
        if stack: # there is root parent
            return stack[-1] 
        else:   # just one node
            return TreeNode(int(val))
