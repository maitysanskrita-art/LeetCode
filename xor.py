class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {n & mask for n in nums}
            candidate = ans | (1 << i)

            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    ans = candidate
                    break

        return ans