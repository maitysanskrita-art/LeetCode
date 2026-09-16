class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Number of letters and words must be same
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):

            # Check pattern letter -> word
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False

            # Check word -> pattern letter
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False

            char_to_word[ch] = word
            word_to_char[word] = ch

        return True