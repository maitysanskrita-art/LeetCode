class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=set()
        diagonal1=set()
        diagonal2=set()
        count=0
        def backtrack(row):
            nonlocal count
            if row==n:
                count+=1
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
                backtrack(row+1)
                cols.remove(col)
                diagonal1.remove(row-col)
                diagonal2.remove(row+col)
        backtrack(0)
        return count
        