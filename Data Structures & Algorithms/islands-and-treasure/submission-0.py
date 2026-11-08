class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #we do bfs
        #instead of going to find treasure, we start from treasure
        #then for every step, we add 1 if INF 

        INF = 2**31 - 1 #constant 
        q=deque()

        height, width = len(grid), len(grid[0])

        #first add all treasurecells to the queue
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r,c = q.popleft() 
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                #check bounds
                if nr < 0 or nr >= height or nc < 0 or nc >= width:
                    continue
                
                #visit unvisited (INF)
                if grid[nr][nc] != INF:
                    continue
                
                #compute distance
                grid[nr][nc] = grid[r][c]+1

                q.append((nr,nc))
        


            