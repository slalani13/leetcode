class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        graph = self.graph(edges)
        maxSum = float("-inf")
        for key,edgeList in graph.items():
            curSum = vals[key]
            
            if len(edgeList) > k:
                newList = []
                for node in edgeList:
                    newList.append(vals[node])
                newList.sort()
                idx = -1
                for i in range(k):
                    if newList[idx] > 0:
                        curSum += newList[idx]
                    idx -=1
            else:
                for node in edgeList:
                    if vals[node] > 0:
                        curSum += vals[node]
            
            maxSum = max(curSum, maxSum)

        return maxSum
    
    def graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        high = max(graph.keys())
        for i in range(high):
            if i not in graph:
                graph[i] = []

        return graph
