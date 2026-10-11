
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        start += (n - 1) // digits
        s = str(start)
        return int(s[(n - 1) % digits])
