class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:

        # Area of first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)

        # Area of second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)

        # Find overlapping width
        overlap_width = min(ax2, bx2) - max(ax1, bx1)

        # Find overlapping height
        overlap_height = min(ay2, by2) - max(ay1, by1)

        # If rectangles overlap
        if overlap_width > 0 and overlap_height > 0:
            overlap_area = overlap_width * overlap_height
        else:
            overlap_area = 0

        # Total area
        return area1 + area2 - overlap_area