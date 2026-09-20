class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:

        def get_max(nums, length):
            drop = len(nums) - length
            stack = []

            for num in nums:
                while stack and drop > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        def greater(a, b):
            return a > b

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)

            candidate = merge(a[:], b[:])

            if candidate > answer:
                answer = candidate

        return answer