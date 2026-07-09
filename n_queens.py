class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        cols=set()
        diagonal1=set()
        diagonal2=set()
        board=[["." for _ in range(n)] for _ in range(n)]
        def backtrack(row):
            if row==n:
                copy=["".join(r) for r in board]
                result.append(copy)
                return
            for col in range(n):
                if col in cols:
                    continue
                if (row-col) in diagonal1:
                    continue
                if (row+col) in diagonal2:
                    continue
                cols.add(col)
                diagonal1.add(row-col)
                diagonal2.add(row+col)
                board[row][col]="Q"
                backtrack(row+1)
                board[row][col]="."
                cols.remove(col)
                diagonal1.remove(row-col)
                diagonal2.remove(row+col)
        backtrack(0)
        return result
        
        