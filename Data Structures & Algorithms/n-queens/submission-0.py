class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def checkQueen(r, c):
            # Check vertically upward
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            # Check upper-left diagonal
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            # Check upper-right diagonal
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if checkQueen(r, c):
                    board[r][c] = "Q"

                    dfs(r + 1)

                    board[r][c] = "."

        dfs(0)
        return res