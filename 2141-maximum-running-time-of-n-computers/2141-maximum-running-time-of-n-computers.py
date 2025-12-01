class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        left, right = 0, total // n

        def can_run(t):
            usable = 0
            for b in batteries:
                usable += min(b, t)
            return usable >= n * t

        while left < right:
            mid = (left + right + 1) // 2
            if can_run(mid):
                left = mid
            else:
                right = mid - 1

        return left