class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)

        overlap_width = min(ax2, bx2) - max(bx1, ax1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        if overlap_width > 0 and overlap_height > 0:
            return area_1 + area_2 - (overlap_width * overlap_height)
        else:
            return area_1 + area_2