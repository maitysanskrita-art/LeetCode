class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start, path):

            # If we have 4 parts and used all characters
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            # Try taking 1, 2, or 3 digits
            for length in range(1, 4):

                # If substring goes out of bounds
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Number must be between 0 and 255
                if int(part) > 255:
                    continue

                # Choose this part
                path.append(part)

                # Recurse for the remaining string
                backtrack(start + length, path)

                # Undo the choice
                path.pop()

        backtrack(0, [])
        return result