class NumArray:

    def __init__(self, nums: list[int]):
        self.sum = [0]

        for num in nums:
            self.sum.append(self.sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]