class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0

        while n >= rows + 1:
            rows += 1
            n -= rows

        return rows