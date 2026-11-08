class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        minutes = 0 
        fresh = 0

        q = deque() 

        #get all rotten and find fresh 
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1


        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh > 0:  #while there is still fresh available
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                
                #check bounds
                    if nr<0 or nr >= height or nc < 0 or nc>=width:
                        continue 
                
                #check if empty 
                    if grid[nr][nc] != 1:
                        continue 
            
            #this is fresh fruit so turn rotten and then +1
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))

            minutes+=1
        
        if fresh == 0:
            return minutes
        else:
            return -1



        