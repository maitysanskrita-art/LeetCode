class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0
        right = 0

        # Find how many '(' and ')' must be removed
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def backtrack(i, path, balance, lremove, rremove):
            if i == len(s):
                if balance == 0 and lremove == 0 and rremove == 0:
                    ans.add("".join(path))
                return

            ch = s[i]

            if ch == '(':
                # Remove this '('
                if lremove > 0:
                    backtrack(i + 1, path, balance, lremove - 1, rremove)

                # Keep this '('
                path.append(ch)
                backtrack(i + 1, path, balance + 1, lremove, rremove)
                path.pop()

            elif ch == ')':
                # Remove this ')'
                if rremove > 0:
                    backtrack(i + 1, path, balance, lremove, rremove - 1)

                # Keep this ')' only if it has a matching '('
                if balance > 0:
                    path.append(ch)
                    backtrack(i + 1, path, balance - 1, lremove, rremove)
                    path.pop()

            else:
                path.append(ch)
                backtrack(i + 1, path, balance, lremove, rremove)
                path.pop()

        backtrack(0, [], 0, left, right)

        return list(ans)