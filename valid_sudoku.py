class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        boxes={}
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                box=(r//3,c//3)
                if r not in rows:
                    rows[r]=set()
                if c not in cols:
                    cols[c]=set()
                if box not in boxes:
                    boxes[box]=set()
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True
        