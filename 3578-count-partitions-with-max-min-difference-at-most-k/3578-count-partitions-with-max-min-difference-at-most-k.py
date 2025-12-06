class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0

        # 1) compute r[i]: max index r >= i with max(nums[i..r]) - min(nums[i..r]) <= k
        r = [-1] * n
        maxD = deque()  # holds indices, nums[maxD] decreasing
        minD = deque()  # holds indices, nums[minD] increasing
        right = -1

        for left in range(n):
            # extend right as far as valid
            while right + 1 < n:
                nxt = right + 1
                val = nums[nxt]
                while maxD and nums[maxD[-1]] < val:
                    maxD.pop()
                maxD.append(nxt)
                while minD and nums[minD[-1]] > val:
                    minD.pop()
                minD.append(nxt)

                if nums[maxD[0]] - nums[minD[0]] <= k:
                    right = nxt
                else:
                    # undo adding nxt
                    if maxD and maxD[-1] == nxt:
                        maxD.pop()
                    if minD and minD[-1] == nxt:
                        minD.pop()
                    break

            r[left] = right

            # move left forward: pop index left from fronts if present
            if maxD and maxD[0] == left:
                maxD.popleft()
            if minD and minD[0] == left:
                minD.popleft()

            # if window became empty (right < left), reset right to left
            if right < left:
                right = left

        # 2) dp using suffix sums
        # dp[i] = ways to partition suffix starting at i. dp[n] = 1
        dp = [0] * (n + 1)
        dp[n] = 1
        # suffix_sum[i] = dp[i] + dp[i+1] + ... + dp[n]
        suffix = [0] * (n + 2)
        suffix[n] = dp[n]
        suffix[n+1] = 0

        for i in range(n - 1, -1, -1):
            rightmost = r[i]
            if rightmost < i:
                dp[i] = 0
            else:
                # dp[i] = sum(dp[j+1] for j in [i..rightmost])
                # which equals sum dp[t] for t in [i+1 .. rightmost+1]
                left_idx = i + 1
                right_idx = rightmost + 1
                total = suffix[left_idx]
                subtract = suffix[right_idx + 1] if (right_idx + 1) <= n else 0
                dp[i] = (total - subtract) % MOD

            suffix[i] = (dp[i] + suffix[i+1]) % MOD

        return dp[0] % MOD