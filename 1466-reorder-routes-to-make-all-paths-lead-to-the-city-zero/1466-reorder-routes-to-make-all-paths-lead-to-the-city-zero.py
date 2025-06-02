class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        swaps = [0]
        seen = set()
        graph = defaultdict(list)
        for start, end in connections:
            graph[start].append((end, -1))
            graph[end].append((start, 1))
        # -1 means outward pointing arrow
        # 1 means inward pointing arrow    
# {0: [(1, -1), (4, 1)], 1: [(0, 1), (3, -1)], 2: [(3, -1)], 3:[(1, 1), (2, 1)] 4: [(0, 1), (5, -1)], 5:[(4, -1)] }

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei, dir in graph[node]:
                if nei not in seen:
                    if dir == -1:
                        swaps[0] += 1
                    dfs(nei)
        
        dfs(0)
        return swaps[0]
# {0: [(1, -1), (4, 1)], 1: [(0, 1), (3, -1)], 2: [(3, -1)], 3:[(1, 1), (2, 1)] 4: [(0, 1), (5, -1)], 5:[(4, -1)] }
# seen = (0,1)
# swap = 2
        # dfs(0) - graph[0][0] dfs(1)
        # dfs(1)
