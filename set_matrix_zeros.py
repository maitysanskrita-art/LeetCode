lass Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        # Find all rows and columns containing 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Set rows to 0
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        # Set columns to 0
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        