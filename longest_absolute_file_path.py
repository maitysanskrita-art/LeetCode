class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]
        ans = 0

        for line in input.split("\n"):
            level = line.count("\t")
            name = line.lstrip("\t")

            while len(stack) > level + 1:
                stack.pop()

            length = stack[-1] + len(name)

            if "." in name:
                ans = max(ans, length)
            else:
                stack.append(length + 1)

        return ans