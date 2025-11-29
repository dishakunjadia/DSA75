class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        from math import gcd

        n = len(points)
        if n <= 2:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalize slope direction (unique representation)
                if dx < 0:
                    dx = -dx
                    dy = -dy
                    
                elif dx == 0:  # vertical line
                    dy = 1
                
                slopes[(dx, dy)] += 1
            
            max_points = max(max_points, max(slopes.values(), default=0) + duplicates + 1)
        
        return max_points