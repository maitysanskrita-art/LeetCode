class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2

            left, count1 = merge_sort(arr[:mid])
            right, count2 = merge_sort(arr[mid:])

            count = count1 + count2

            j = 0
            k = 0

            for x in left:
                while j < len(right) and right[j] - x < lower:
                    j += 1

                while k < len(right) and right[k] - x <= upper:
                    k += 1

                count += k - j

            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        return merge_sort(prefix)[1]