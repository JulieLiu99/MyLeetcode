class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        """
        Find the lower and upper hulls which together form the convex hull of all points.
        
        Process the points in sorted order:
        left->right & down->up: lower hull
        right->left & up->down: upper hull
        
        Lower hull needs counter-clockwise turns. If A is above OB -> remove A from fence.
        __/ B
        O A
        
        We can do this process again with the points in reverse order.
        Upper hull needs clockwise turns. If A is below OB -> remove A from fence.
        O__A
           \B
          
        Time O(n)
        Space O(1)
        
        """
        
        trees = sorted([(x, y) for x, y in trees])
        

        # (b[1] - o[1])/(b[0] - o[0]) ?= (a[1] - o[1])/(a[0] - o[0])
        # if two segments have same slope -> OAB collinear: return 0
        # if OB has more positive slope than OA -> OAB makes a counter-clockwise turn: return +
        # if OB has less positive slope than OA -> OAB makes a clockwise turn: return -
        def sign(O, A, B):
            return (A[0]-O[0]) * (B[1]-O[1]) - (B[0]-O[0]) * (A[1]-O[1])
        
        def build(trees):
            
            hull = []
            
            for p in trees:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)

            return hull
        
        # Concatenation of the lower and upper hulls gives the convex hull.
        return list(set(build(trees) + build(trees[::-1])))
