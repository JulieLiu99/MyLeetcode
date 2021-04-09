# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
            
        # Iterative
        #
        # Save the construction path in a stack.
        # In each loop,
        # Get the number level of '-'
        # Get the value val of node to add.
        #
        # If size of stack is bigger than level of node,
        # pop the stack until it's not.
        #
        # Finally return the first element in the stack, as it's root of tree.
        #
        # Time O(N)
        # Space O(N)
        
        
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':   # get level
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':   # get val
                val, i = val + S[i], i + 1
            while len(stack) > level:   # size of stack = level
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        
        
       
"""
Recursive (regex for dict)
"""
"""
import re

class Solution(object):
    def recoverFromPreorder(self, S):
        
        # this entire block of code is just to count level for each value
        # could be written in regex:
        # vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]
        
        vals = []
        level = 0
        save_level = 0
        val = ""
        i = 0
        while(i<len(S)):
            if S[i] == "-" and level==0:
                vals.append((save_level,int(val)))
                val=""
                level += 1
            elif S[i] == "-":
                level += 1
            elif S[i] != "-" and val=="":
                save_level = level
                level = 0
                val += S[i]
            else:
                val += S[i]
            i += 1
        vals.append((save_level,int(val)))
        vals.reverse()  

        def fn(level):
            if not vals or level != vals[-1][0]: return None
            node = TreeNode(vals.pop()[1])
            node.left = fn(level+1)
            node.right = fn(level+1)
            return node
        return fn(0)
"""
