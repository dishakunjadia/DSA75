#class Solution(object):
    #def maxStability(self, n, edges, k):
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True


class Solution:
    def maxStability(self, n, edges, k):
        
        def can(mid):
            uf = UnionFind(n)
            upgrades = 0
            count = 0

            # add must edges
            for u,v,s,m in edges:
                if m == 1:
                    if s < mid:
                        return False
                    if not uf.union(u,v):
                        return False
                    count += 1

            optional = []

            for u,v,s,m in edges:
                if m == 0:
                    optional.append((u,v,s))

            # try without upgrade
            for u,v,s in optional:
                if s >= mid:
                    if uf.union(u,v):
                        count += 1

            # try with upgrade
            for u,v,s in optional:
                if s < mid and s*2 >= mid:
                    if upgrades < k and uf.union(u,v):
                        upgrades += 1
                        count += 1

            return count == n-1

        left = 0
        right = max(s for _,_,s,_ in edges) * 2
        ans = -1

        while left <= right:
            mid = (left+right)//2

            if can(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans


        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        