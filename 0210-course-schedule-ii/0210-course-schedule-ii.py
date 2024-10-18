class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo_sort = []
        g = defaultdict(list)
        for a,b in prerequisites:
            g[b].append(a)
        
        # UNVISITED = 0, VISITING = 1, VISITED = 2
        states = [0] * numCourses
        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            states[node] = 1
            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            states[node] = 2
            topo_sort.append(node)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return topo_sort[::-1]

        