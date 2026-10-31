class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #key here is doesn't need to be solvable
        #so just need ot check 1-9 for each row, column, 3x3 square
        #brute force
        #check rows
        
        #check rows
        for i in range(9):
            row_check = []
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_check:
                    return False
                else: 
                    row_check.append(board[i][j])
        
        #check columns
        for i in range(9):
            col_check = []
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_check:
                    return False
                else: 
                    col_check.append(board[j][i])

        #check 3x3
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square_check = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in square_check:
                            return False
                        else:
                            square_check.append(board[i][j])

        return True


