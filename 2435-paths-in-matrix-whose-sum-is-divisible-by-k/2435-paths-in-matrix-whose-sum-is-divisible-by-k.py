class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][r] = ways to reach cell (i,j) with remainder r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        # initialize
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                mod_val = val % k

                # from top
                if i > 0:
                    for r in range(k):
                        new_r = (r + mod_val) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD

                # from left
                if j > 0:
                    for r in range(k):
                        new_r = (r + mod_val) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD

        return dp[m-1][n-1][0]
