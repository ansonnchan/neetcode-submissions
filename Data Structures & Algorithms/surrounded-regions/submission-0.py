class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #brute force O(m*n)
        for r in range(1,len(board)-1):
            for c in range(1,len(board[0])-1):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        
                
        