class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        mp = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                left = word[:j]
                right = word[j:]

                # If left is palindrome, reverse(right) can come before word
                if left == left[::-1]:
                    rev = right[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([mp[rev], i])

                # If right is palindrome, reverse(left) can come after word
                if j != n and right == right[::-1]:
                    rev = left[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([i, mp[rev]])

        return ans