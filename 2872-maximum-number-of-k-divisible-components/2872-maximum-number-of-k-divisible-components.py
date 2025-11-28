class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict, deque
    
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        components = 0
        
        def dfs(node, parent):
            nonlocal components
            subtotal = values[node]
            
            for child in graph[node]:
                if child == parent:
                    continue
                remainder = dfs(child, node)
                subtotal += remainder
            
            if subtotal % k == 0:
                components += 1
                return 0  # cut here
            else:
                return subtotal % k  # pass up remainder
        
        dfs(0, -1)
        return components
            