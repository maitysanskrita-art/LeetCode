class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> list[list[int]]:
        if not self.nums:
            return []

        nums = sorted(self.nums)
        result = []

        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                result.append([start, end])
                start = nums[i]
                end = nums[i]

        result.append([start, end])

        return result