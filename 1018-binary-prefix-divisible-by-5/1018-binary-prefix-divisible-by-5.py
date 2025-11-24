class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        remainder = 0

        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            ans.append(remainder == 0)

        return ans