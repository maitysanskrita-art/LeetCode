class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        odd_found = False

        for freq in __import__('collections').Counter(s).values():
            count += (freq // 2) * 2
            if freq % 2 == 1:
                odd_found = True

        if odd_found:
            count += 1

        return count