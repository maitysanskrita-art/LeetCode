class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # 8 possible directions around a cell
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(rows):
            for c in range(cols):

                # Count live neighbors
                live = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live += 1

                # Current cell is alive
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = 2   # 1 -> 0

                # Current cell is dead
                else:
                    if live == 3:
                        board[r][c] = 3   # 0 -> 1

        # Convert temporary values to final values
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1