class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n
        for i in range(n):
            idx = (i + nums[i]) % n 
            result[i] = nums[idx]
        return result
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        