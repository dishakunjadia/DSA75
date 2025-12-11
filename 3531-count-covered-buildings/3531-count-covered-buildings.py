class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        from collections import defaultdict
        import bisect

        row = defaultdict(list)
        col = defaultdict(list)

        # Build row and column maps
        for x, y in buildings:
            row[x].append(y)
            col[y].append(x)

        # Sort for binary search
        for x in row:
            row[x].sort()
        for y in col:
            col[y].sort()

        covered = 0

        # Check each building
        for x, y in buildings:
            ys = row[x]
            xs = col[y]

            i = bisect.bisect_left(ys, y)
            j = bisect.bisect_left(xs, x)

            has_left = i > 0
            has_right = i < len(ys) - 1
            has_above = j > 0
            has_below = j < len(xs) - 1

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered