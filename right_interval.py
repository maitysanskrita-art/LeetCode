
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        import bisect

        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        result = []

        for start, end in intervals:
            pos = bisect.bisect_left(starts, (end, -1))

            if pos < len(starts):
                result.append(starts[pos][1])
            else:
                result.append(-1)

        return result
