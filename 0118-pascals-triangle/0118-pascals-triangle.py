class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            if r == 0:
                triangle.append([1])
            else:
                prev = triangle[-1]
                row = [1]
                for i in range(1, r):
                    row.append(prev[i - 1] + prev[i])
                row.append(1)
                triangle.append(row)

        return triangle

        

    