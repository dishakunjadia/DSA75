class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = len(source)

        # Map all patterns to ids
        patterns = {}
        pid = 0
        for s in original + changed:
            if s not in patterns:
                patterns[s] = pid
                pid += 1

        m = pid
        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = patterns[o]
            v = patterns[c]
            dist[u][v] = min(dist[u][v], w)

        # Floyd–Warshall
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Build Trie on original
        root = TrieNode()
        for s in original:
            node = root
            for c in s:
                node = node.children.setdefault(c, TrieNode())
            node.idx = patterns[s]

        # DP
        dp = [INF]*(n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            # No operation
            if source[i] == target[i]:
                dp[i] = dp[i+1]

            # Try substring conversions
            node = root
            j = i
            while j < n and source[j] in node.children:
                node = node.children[source[j]]
                j += 1
                if node.idx != -1:
                    src_id = node.idx
                    tgt_sub = target[i:j]
                    if tgt_sub in patterns:
                        tgt_id = patterns[tgt_sub]
                        if dist[src_id][tgt_id] < INF:
                            dp[i] = min(dp[i], dist[src_id][tgt_id] + dp[j])

        return -1 if dp[0] == INF else dp[0]
