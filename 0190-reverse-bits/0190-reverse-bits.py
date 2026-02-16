class Solution(object):
    def reverseBits(self, n):
        result = 0 
        for _ in range(32):
            result <<= 1 
            result |= (n & 1)
            n >>= 1
        return result 
        """
        :type n: int
        :rtype: int
        """
        