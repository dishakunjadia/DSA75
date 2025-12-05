class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        countZero = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                countZero += 1
            
            while countZero > 1:
                if nums[left] == 0:
                    countZero -= 1
                left += 1
            
            # window valid, store length - 1 because we must delete one element
            max_len = max(max_len, right - left + 1 - 1)
        
        return max_len