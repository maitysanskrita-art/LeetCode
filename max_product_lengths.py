class Solution:
    def maxProduct(self, words: list[str]) -> int:
        max_product = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if set(words[i]).isdisjoint(set(words[j])):
                    max_product = max(max_product,
                                      len(words[i]) * len(words[j]))

        return max_product