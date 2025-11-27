class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0   # prefix sum before starting (index 0)
        ans = -float('inf')

        # iterate indices starting at 1 so that length = r - l works out
        for i, num in enumerate(nums, start=1):
            prefix += num
            mod = i % k
            # candidate subarray ending at i whose length is divisible by k
            ans = max(ans, prefix - min_prefix[mod])
            # update minimum prefix for this remainder class
            min_prefix[mod] = min(min_prefix[mod], prefix)

        return int(ans)