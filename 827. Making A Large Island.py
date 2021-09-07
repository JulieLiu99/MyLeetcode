class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        """
        Graph: DFS
        
        0: water
        1: land
        
        Time O(m*n)
        Space O(m*n)
        
        """
        # mark cells that form one land with one color
        # track area of the land
        def dfs(i, j, color):
                if not color in area:
                    area[color] = 0
                grid[i][j] = color
                seen.add((i, j))
                area[color] += 1

                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                        if (x, y) not in seen:
                            dfs(x, y, color)

		# main
        color = 0
        area = {}
        seen = set()
        m, n = len(grid), len(grid[0])
        
        # check if water exists
        checked = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    checked = True
                    break
        if not checked:
            return m * n
        
        # dfs for connected lands, mark them with different colors
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in seen:
                    color += 1
                    dfs(i, j, color)
        
        # go through all 0s and calculate land around them if they are converted
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_land_id = set()
                    for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                            unique_land_id.add(grid[x][y])
                    # current 0 converted to 1
                    cur_area = 1
                    for land_id in unique_land_id:
                        cur_area += area[land_id]
                    max_area = max(max_area, cur_area)
        return max_area
