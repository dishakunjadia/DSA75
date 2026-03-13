class Solution(object):
    def minNumberOfSeconds(self, height, Times):
        lo = 1
        hi = 10000000000000000

        while lo < hi:
            mid = (lo + hi) >> 1
            totalLayers = 0

            for t in Times:
                if totalLayers >= height:
                    break

                layers = int(((2.0 * mid) / t + 0.25) ** 0.5 - 0.5)
                totalLayers += layers

            if totalLayers >= height:
                hi = mid
            else:
                lo = mid + 1

        return lo
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        