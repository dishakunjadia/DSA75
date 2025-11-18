class Solution:
    def pivotInteger(self, n: int) -> int:
        if n <= 0:
            return -1
        val = n*(n+1)//2
        x = math.isqrt(val)
        return x if x*x == val else -1

        