class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def max_consecutive(arr):
            if not arr:
                return 1
            arr.sort()
            longest = 1 
            curr = 1 
            for i in range(1,len(arr)):
                if arr[i] == arr[i-1] + 1:
                    curr += 1 
                    longest = max(longest, curr)
                else:
                    curr = 1
            return longest + 1
        maxH = max_consecutive(hBars)
        maxV = max_consecutive(vBars)

        side = min(maxH, maxV)
        return side * side


        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        