class Solution(object):
    def sumFourDivisors(self, nums):
        ans = 0

        for x in nums:
            count = 0
            total = 0
            d = 1
            while d * d <= x:
                if x % d == 0:
                    d1 = d
                    d2 = x // d

                    count += 1
                    total += d1

                    if d1 != d2:
                        count += 1
                        total += d2

                    if count > 4:
                        break
                d += 1

            if count == 4:
                ans += total

        return ans


        """
        :type nums: List[int]
        :rtype: int
        """
        