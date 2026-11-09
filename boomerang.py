class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for i in range(len(points)):
            count = {}

            for j in range(len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distance = dx * dx + dy * dy

                count[distance] = count.get(distance, 0) + 1

            for value in count.values():
                result += value * (value - 1)

        return result