class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        left = nums[:mid][::-1]
        right = nums[mid:][::-1]

        for i in range(len(left)):
            nums[2 * i] = left[i]
            if 2 * i + 1 < n:
                nums[2 * i + 1] = right[i]