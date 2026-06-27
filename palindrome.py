class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=str(x)
        reverse=original[::-1]
        if original==reverse:
            return True
        else:
            return False