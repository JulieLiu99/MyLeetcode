# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    BFS
    
    Time O(n)
    Space O(n)
    
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(str(node.val) if node else '#')
            if node:
                q.append(node.left)
                q.append(node.right)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] is not '#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
        
            if nodes[i] is not '#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root

    """
    Preorder traversal - DFS
    
    Time O(n)
    Space O(n)
    
    """
#     def serialize(self, root):
#         if root == None: return "#"
#         return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

#     def deserialize(self, data):
#         # data "1,2,#,#,3,4,#,#,5,#,#""
#         nodes = data.split(",")
#         self.i = 0

#         def dfs():
#             if self.i == len(nodes): 
#                 return None
#             nodeVal = nodes[self.i]
#             self.i += 1
#             if nodeVal == "#": 
#                 return None
            
#             root = TreeNode(int(nodeVal))
#             root.left = dfs()
#             root.right = dfs()
#             return root

#         return dfs()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
