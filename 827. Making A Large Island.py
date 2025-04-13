class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        """
        Graph: DFS
        
        0: water
        1: land
        >= 2: visited land, marked with color id
        
        Time O(m*n)
        Space O(m*n)
        
        """
        # mark cells that form one land with one color
        # track area of the land
        def dfs(i, j, color):
            grid[i][j] = color
            area[color] += 1
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y, color)

		# main
        color = 1
        area = collections.defaultdict(int)
        m, n = len(grid), len(grid[0])
        
        # check if water exists
        water = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    water = True
                    break
        if not water:
            return m * n
        
        # dfs for connected lands, mark them with different colors
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    color += 1
                    dfs(i, j, color)
        
        # go through all 0s and calculate land around them if they are converted
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_land_id = set()
                    for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                            neighbor_land_id.add(grid[x][y])
                    # current 0 converted to 1
                    cur_area = 1
                    for land_id in neighbor_land_id:
                        cur_area += area[land_id]
                    max_area = max(max_area, cur_area)
        return max_area
