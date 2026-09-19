class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.add(i + 1, nums[i])

    def add(self, i: int, val: int):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, diff)

    def prefixSum(self, i: int) -> int:
        total = 0

        while i > 0:
            total += self.tree[i]
            i -= i & -i

        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)