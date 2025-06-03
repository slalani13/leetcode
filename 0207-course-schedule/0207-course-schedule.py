class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a topological ordering for [0,  1] would be 1 -> 0
        # create adj list of nodes
        # find in-degree of each course
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        q = deque()
        for idx, course in enumerate(indegree):
            if course == 0:
                q.append(idx)
        # [0, 0]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return True if sum(indegree) == 0 else False

