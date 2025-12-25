class Solution:
    """
    Enumerate all possible ways to divide the grid into 3 non-overlapping sections

    For each calculate the areas of bounding boxes

    Time O(n^2 m^2)
    Space O(nm)
    """
    def bbox_area(self, grid: List[List[int]], r1: int, r2: int, c1: int, c2: int) -> int:
        rows = []
        cols = []

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        if not rows:
            return float("inf")

        return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)

    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = rows * cols

        # three horizontal rectangles
        for r1 in range(rows-2): # up to rows-3
            for r2 in range(r1+1, rows-1): ## up to rows-2
                ans = min(
                    ans,
                    self.bbox_area(grid, 0, r1, 0, cols-1)
                    + self.bbox_area(grid, r1+1, r2, 0, cols-1)
                    + self.bbox_area(grid, r2+1, rows-1, 0, cols-1),
                )


        # three vertical rectangles
        for c1 in range(cols-2): # up to cols-3
            for c2 in range(c1+1, cols-1): # up to cols-2
                ans = min(
                    ans,
                    self.bbox_area(grid, 0, rows-1, 0, c1)
                    + self.bbox_area(grid, 0, rows-1, c1+1, c2)
                    + self.bbox_area(grid, 0, rows-1, c2+1, cols-1),
                )

        # top full + bottom split
        for r in range(rows-1):
            for c in range(cols-1):
                ans = min(
                    ans,
                    self.bbox_area(grid, 0, r, 0, cols-1)
                    + self.bbox_area(grid, r+1, rows-1, 0, c)
                    + self.bbox_area(grid, r+1, rows-1, c+1, cols-1),
                )

        # bottom full + top split
        for r in range(rows-1):
            for c in range(cols-1):
                ans = min(
                    ans,
                    self.bbox_area(grid, r+1, rows-1, 0, cols-1)
                    + self.bbox_area(grid, 0, r, 0, c)
                    + self.bbox_area(grid, 0, r, c+1, cols-1),
                )

        # left full + right split
        for c in range(cols-1):
            for r in range(rows-1):
                ans = min(
                    ans,
                    self.bbox_area(grid, 0, rows-1, 0, c)
                    + self.bbox_area(grid, 0, r, c+1, cols-1)
                    + self.bbox_area(grid, r+1, rows-1, c+1, cols-1),
                )

        # right full + left split
        for c in range(cols-1):
            for r in range(rows-1):
                ans = min(
                    ans,
                    self.bbox_area(grid, 0, rows-1, c+1, cols-1)
                    + self.bbox_area(grid, 0, r, 0, c)
                    + self.bbox_area(grid, r+1, rows-1, 0, c),
                )

        return ans
