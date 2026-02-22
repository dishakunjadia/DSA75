class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
    
    # Collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
    
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        