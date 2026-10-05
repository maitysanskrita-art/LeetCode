class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(num):
            if num > n:
                return

            result.append(num)

            for i in range(10):
                next_num = num * 10 + i

                if next_num > n:
                    return

                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result