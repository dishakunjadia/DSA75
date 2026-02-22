class Solution(object):
    def binaryGap(self, n):
        last  = -1
        max_gap = 0
        position = 0 

        while n > 0:
            if n & 1:
                if last != -1:
                    max_gap = max(max_gap, position - last)
                last = position
            n >>= 1 
            position += 1
        return max_gap
                
        """

        :type n: int
        :rtype: int
        """
        