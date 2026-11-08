
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter()
        result = []

        for i in range(len(s)):
            window_count[s[i]] += 1

            if i >= len(p):
                left_char = s[i - len(p)]
                window_count[left_char] -= 1

                if window_count[left_char] == 0:
                    del window_count[left_char]

            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result
