class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.graph(edges)
        visited = set()
        return self.bfs(graph, source, destination, visited)
    
    def graph(self, edgeList):
        graph = defaultdict(list)
        for edge in edgeList:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    # def dfs(self, graph, src, dest, visited):
    #     if src == dest:
    #         return True
    #     if src in visited:
    #         return False
    #     visited.add(src)
    #     for neighbor in graph[src]:
    #         if self.dfs(graph, neighbor, dest, visited):
    #             return True
    #     return False

    def bfs(self, graph, src, dest, visited):
        
        queue = deque()
        queue.append(src)
        visited.add(src)

        while queue:
            node = queue.popleft()
            if node == dest:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
