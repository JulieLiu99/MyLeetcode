"""
Segment Tree

Each node stores the left and right endpoint of an interval and the sum of that interval. 
Each internal node stores sum of leaves under it.

Creating the tree takes O(n) time. Query and updates are both O(log n).
Space O(n)

"""

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
    def __init__(self, nums):
        def createTree(nums, l, r):
            
            if l > r:   #base case
                return None
                
            if l == r:  #leaf node
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of elements (start, end)
            root.total = root.left.total + root.right.total
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
            
    def update(self, index, val):
        def updateVal(root, i, val):
            
            #Base case. Update value in leaf.
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            if i <= mid:     #leaf must be in the left subtree
                updateVal(root.left, i, val)
            else:            #otherwise, the right subtree
                updateVal(root.right, i, val)
            
            #Propogate the values after recursive call returns
            root.total = root.left.total + root.right.total
            return root.total
        
        return updateVal(self.root, index, val)

    
    def sumRange(self, left, right):
        def rangeSum(root, i, j):
            
            #If range matches with the node interval, return value
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            if j <= mid:        # entire interval in the left subtree
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:  # right subtree
                return rangeSum(root.right, i, j)
            else:               # interval is split
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, left, right)
                


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
