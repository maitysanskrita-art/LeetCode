class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0

        while i < len(chars):
            count = 0
            ch = chars[i]

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1

            chars[index] = ch
            index += 1

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index