class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        row_map = {}

        for row in grid:
            row_tuple = tuple(row)
            row_map[row_tuple] = row_map.get(row_tuple, 0) + 1 
        count = 0

        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            col_tuple = tuple(col)
            count += row_map.get(col_tuple, 0)
        return count
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        