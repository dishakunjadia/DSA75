class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4: 
            return False 
        i = 0 

        # increasing 
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1 
        
        # p must exist and not be at the end 
        if i == 0 or i == n - 1:
            return False 
        # decreasing 
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1 
        # q must exist and not be at the end 
        if i == n-1:
            return False
        # strictly increasing again 
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1 
        # must consume entire array 
        return i == n-1
        