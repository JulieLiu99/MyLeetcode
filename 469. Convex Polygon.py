class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        
        def direction(a,b,c):
            return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        
        d = None # direction of graph
        
        for i in range(len(points)):
            a = direction(points[i-2], points[i-1], points[i])
            if a == 0: # collinear
                continue
            if d == None: 
                d = a
            elif a*d < 0: # concave
                    return False
        
        return True
