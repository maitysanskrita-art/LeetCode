class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        points = set()

        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)

            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

            for point in corners:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        expected_area = (max_x - min_x) * (max_y - min_y)

        if area != expected_area:
            return False

        return points == {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }