class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        index = [0] * len(primes)

        for i in range(1, n):
            next_num = float('inf')

            for j in range(len(primes)):
                next_num = min(next_num, ugly[index[j]] * primes[j])

            ugly[i] = next_num

            for j in range(len(primes)):
                if ugly[index[j]] * primes[j] == next_num:
                    index[j] += 1

        return ugly[n - 1]