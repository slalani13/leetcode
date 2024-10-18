class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        courses = prerequisites
        for a,b in courses:
            graph[b].append(a)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        nodes = [UNVISITED] * numCourses
        def dfs(node):
            if nodes[node] == VISITING:
                return False
            elif nodes[node] == VISITED:
                return True
            nodes[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            nodes[node] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
