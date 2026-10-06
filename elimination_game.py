class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        first = 1
        step = 1
        remaining = n

        while remaining > 1:
            if left or remaining % 2 == 1:
                first += step

            remaining //= 2
            step *= 2
            left = not left

        return first