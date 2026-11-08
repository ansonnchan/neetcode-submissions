class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #similar to no.islands 
        #instead of adding islands, we find the area instead

        height, width = len(grid), len(grid[0])
        
        def dfs(r, c): #returns the area
            #base case again
            if (r<0 or r >= height or c <0 or c>= width or grid[r][c] == 0):
                return 0

            #mark as visited (this was 1->0)
            grid[r][c] = 0 

            #count current cell 
            area = 1 

            #exlore 4 directions
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
        
            return area

        max_island_area = 0

        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    current_island_area = dfs(r,c)
                    max_island_area = max(max_island_area, current_island_area)
        return max_island_area

            

        