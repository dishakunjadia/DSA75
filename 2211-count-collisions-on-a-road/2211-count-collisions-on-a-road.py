class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        
        # remove leftmost non-colliding L's
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        
        # remove rightmost non-colliding R's
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # all remaining movers will collide
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
        
        return collisions