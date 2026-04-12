class Solution:
    def minimumDistance(self, word: str) -> int:
        INF = float('inf')
        # dp[other] = min cost when current char just typed, other finger at `other`
        # 26 = finger not yet placed (free move)
        dp = {26: 0}  # start: one finger will type first char for free, other not placed

        def dist(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        for i, ch in enumerate(word):
            cur = ord(ch) - ord('A')
            prev = ord(word[i-1]) - ord('A') if i > 0 else 26
            new_dp = {}

            for other, cost in dp.items():
                # Option 1: move the finger that typed prev to cur
                key1 = other
                val1 = cost + dist(prev, cur)
                if key1 not in new_dp or new_dp[key1] > val1:
                    new_dp[key1] = val1

                # Option 2: move the other finger to cur; prev becomes the new "other"
                key2 = prev
                val2 = cost + dist(other, cur)
                if key2 not in new_dp or new_dp[key2] > val2:
                    new_dp[key2] = val2

            dp = new_dp

        return min(dp.values())