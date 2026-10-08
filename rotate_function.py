class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)

        total = sum(nums)
        f = sum(i * nums[i] for i in range(n))

        maximum = f

        for k in range(1, n):
            f = f + total - n * nums[n - k]
            maximum = max(maximum, f)

        return maximum