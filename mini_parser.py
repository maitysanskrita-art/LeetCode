class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        sign = 1

        for ch in s:

            if ch == '[':
                stack.append(NestedInteger())

            elif ch == '-':
                sign = -1

            elif ch.isdigit():
                num += ch

            elif ch == ',' or ch == ']':

                if num:
                    stack[-1].add(NestedInteger(sign * int(num)))
                    num = ""
                    sign = 1

                if ch == ']' and len(stack) > 1:
                    last = stack.pop()
                    stack[-1].add(last)

        return stack[0]