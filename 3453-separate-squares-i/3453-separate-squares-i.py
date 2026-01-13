class Solution(object):
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Helper function: difference between area above and below y
        def area_diff(y):
            above = below = 0.0
            for _, bottom, l in squares:
                top = bottom + l
                area = l * l
                
                if y <= bottom:
                    above += area
                elif y >= top:
                    below += area
                else:
                    below += l * (y - bottom)
                    above += l * (top - y)
            return above - below

        # Binary search bounds
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        # Binary search
        for _ in range(60):  # sufficient for 1e-5 precision
            mid = (low + high) / 2
            if area_diff(mid) > 0:
                low = mid
            else:
                high = mid

        return (low + high) / 2

            """
            :type squares: List[List[int]]
            :rtype: float
            """
            