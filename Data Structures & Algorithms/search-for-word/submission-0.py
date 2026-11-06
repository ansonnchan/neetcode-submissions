class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i): #take in current position (r,c) and i current character we're trying to match at 

            if i == len(word):
                return True 

            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[i]):
                return False #boundary checks, visited, incorrect match
            visited.add((r,c))

            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or 
                     dfs(r, c+1, i+1) or 
                     dfs(r, c-1, i+1))

            visited.remove((r,c))

            return found


        for r in range(rows):
            for c in range(cols):
                 if dfs(r,c,0):
                    return True

        return False 
