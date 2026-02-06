class Solution(object):
    def minRemoval(self, nums, k):

        nums.sort()
        left = 0
        max_window = 1 
        n = len(nums)

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1 
            max_window = max(max_window, right-left+1)
        return n-max_window
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        