"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    """
    BFS
    
    for each node, save node & n_children
    
    """
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                q.append(child)
        return ','.join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([(root, int(nodes[1]))])
        i = 2
        while q:
            node, n_children = q.popleft()
            node.children = []
            for _ in range(n_children):
                child = TreeNode(int(nodes[i]))
                node.children.append(child)
                q.append((child, int(nodes[i+1])))
                i += 2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
