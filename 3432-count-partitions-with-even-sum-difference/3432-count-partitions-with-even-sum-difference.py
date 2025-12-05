class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 2 != 0:
            return 0
        return max(0, len(nums) - 1)
        