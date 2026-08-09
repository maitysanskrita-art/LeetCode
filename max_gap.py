class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        from typing import List
        import math


        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        buckets = [[math.inf, -math.inf] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - mn) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = mn

        for b_min, b_max in buckets:
            if b_min == math.inf:
                continue

            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max

        return max_gap
        