class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Make cols the smaller dimension
        if rows > cols:
            matrix = [list(x) for x in zip(*matrix)]
            rows, cols = cols, rows

        ans = float('-inf')

        for top in range(rows):
            temp = [0] * cols

            for bottom in range(top, rows):
                # Add the current row to the compressed array
                for c in range(cols):
                    temp[c] += matrix[bottom][c]

                # Find max subarray sum <= k
                prefix = [0]
                curr = 0

                for x in temp:
                    curr += x

                    # Need previous prefix >= curr - k
                    import bisect
                    pos = bisect.bisect_left(prefix, curr - k)

                    if pos < len(prefix):
                        ans = max(ans, curr - prefix[pos])

                    bisect.insort(prefix, curr)

        return ans