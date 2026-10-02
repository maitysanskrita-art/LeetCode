class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            i = ord(ch) - ord('a')

            if count[i] == 0:
                return False

            count[i] -= 1

        return True