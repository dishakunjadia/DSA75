class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []

        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            k = 0
            # find the lowest zero bit
            while (p >> k) & 1:
                k += 1

            # construct minimum x
            x = p - (1 << k) + (1 << (k - 1))
            ans.append(x)

        return ans



        """
        :type nums: List[int]
        :rtype: List[int]
        """
        