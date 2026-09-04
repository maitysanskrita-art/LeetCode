class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for a in left:
                    for b in right:
                        if expression[i] == "+":
                            result.append(a + b)
                        elif expression[i] == "-":
                            result.append(a - b)
                        else:
                            result.append(a * b)

        if not result:
            result.append(int(expression))

        return result