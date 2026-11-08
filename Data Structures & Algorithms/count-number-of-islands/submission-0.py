class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        height, width = len(grid), len(grid[0])

        islands = 0

        def dfs(r,c):
            #base case - edge of board or water
            if (r < 0 or r >= height or c < 0 or c >= width or grid[r][c] == "0"):
                return

            #next we mark the current pos as visited 
            grid[r][c] = "0"

            #explore all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(height):
            for c in range(width):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)
        return islands 
                        