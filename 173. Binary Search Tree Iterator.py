# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    Inorder Traversal
    
    Store all vals in an array first
    Maintain a current index
    Querry for next/hasNext by index
    
    Time O(n)
    Space O(n)
    
    """

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = self._inorder(root, [])
        self.idx = -1

    def next(self) -> int:
        self.idx += 1
        return self.inorder[self.idx]

    def hasNext(self) -> bool:
        if self.idx < len(self.inorder) - 1: # before the last node
            return True
        else:
            return False
        
    def _inorder(self, root, arr):
        if not root:
            return
        self._inorder(root.left, arr)
        arr.append(root.val)
        self._inorder(root.right, arr)
        return arr
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
