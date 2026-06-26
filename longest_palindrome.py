class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ""
        resultLength = 0

        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:

                nonlocal result
                nonlocal resultLength

                if (right - left + 1) > resultLength:
                    result = s[left:right+1]
                    resultLength = right - left + 1

                left -= 1
                right += 1

        for i in range(len(s)):

            expand(i, i)

            expand(i, i + 1)

        return result   