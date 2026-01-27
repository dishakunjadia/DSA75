import heapq

class Solution(object):
    def minCost(self, n, edges):
        
        adj = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            rev[v].append((u, w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            # normal edges
            for v, w in adj[u]:
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

            # reversed incoming edges (use switch at u)
            for v, w in rev[u]:
                new_cost = cost + 2 * w
                if dist[v] > new_cost:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]
