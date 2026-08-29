from bisect import bisect_left, insort

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = []

        for i, num in enumerate(nums):
            pos = bisect_left(window, num - valueDiff)

            if pos < len(window) and window[pos] <= num + valueDiff:
                return True

            insort(window, num)

            if i >= indexDiff:
                window.pop(bisect_left(window, nums[i - indexDiff]))

        return False