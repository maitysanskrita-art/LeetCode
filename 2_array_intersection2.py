class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}
        result = []

        # Count elements of nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # Check nums2
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result