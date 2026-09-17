class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                self.sum[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.sum[i][j + 1]
                    + self.sum[i + 1][j]
                    - self.sum[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sum[row2 + 1][col2 + 1]
            - self.sum[row1][col2 + 1]
            - self.sum[row2 + 1][col1]
            + self.sum[row1][col1]
        )