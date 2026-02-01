class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        smallest1 = float('inf')
        smallest2 = float('inf')

        for x in nums[1:]:
            if x < smallest1:
                smallest2 = smallest1
                smallest1 = x

            elif x < smallest2:
                smallest2 = x 
        return first + smallest1 + smallest2