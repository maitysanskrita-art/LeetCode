class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def solve(r, c, size):
            val = grid[r][c]

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        half = size // 2

                        topLeft = solve(r, c, half)
                        topRight = solve(r, c + half, half)
                        bottomLeft = solve(r + half, c, half)
                        bottomRight = solve(r + half, c + half, half)

                        return Node(False, False, topLeft,
                                    topRight, bottomLeft, bottomRight)

            return Node(val == 1, True, None, None, None, None)

        return solve(0, 0, len(grid))