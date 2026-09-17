import heapq

class MedianFinder:

    def __init__(self):
        self.left = []    # max heap
        self.right = []   # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # Keep every number in left <= every number in right
        if self.left and self.right and -self.left[0] > self.right[0]:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        # Balance the sizes
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        if len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2