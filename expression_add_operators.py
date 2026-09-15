class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        def backtrack(index, expression, value, prev):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                # Don't allow numbers like 05
                if i > index and num[index] == '0':
                    break

                current = int(num[index:i + 1])

                if index == 0:
                    backtrack(i + 1, str(current), current, current)
                else:
                    # +
                    backtrack(i + 1, expression + "+" + str(current),
                              value + current, current)

                    # -
                    backtrack(i + 1, expression + "-" + str(current),
                              value - current, -current)

                    # *
                    backtrack(i + 1, expression + "*" + str(current),
                              value - prev + prev * current,
                              prev * current)

        backtrack(0, "", 0, 0)
        return result