class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row,col,num):
            for c in range(9):
                if board[row][c]==num:
                    return False
            for r in range(9):
                if board[r][col]==num:
                    return False
            start_row=(row//3)*3
            start_col=(col//3)*3
            for r in range(start_row,start_row+3):
                for c in range(start_col,start_col+3):
                    if board[r][c]==num:
                        return False
            return True
        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col]==".":
                        for num in "123456789":
                            if is_valid(row,col,num):
                                board[row][col]=num
                                if solve():
                                    return True
                                board[row][col]="."
                        return False
            return True
        solve()       