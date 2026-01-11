class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        col = len(matrix[0])
        height = [0] * col
        max_area = 0 

        for row in matrix: 
            # Updating the histogram
            for i in range(col):
                if row[i] == '1':
                    height[i] += 1 
                else: 
                    height[i] = 0
            # Computing the largest rectangle in the histgram 
            stack = []
            for i in range(col + 1):
                cur_height = height[i] if i < col else 0
                while stack and cur_height < height[stack[-1]]:
                    h= height[stack.pop()]
                    w = i if not stack else i - stack[-1] -1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        