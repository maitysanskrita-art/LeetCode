class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove elements outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result