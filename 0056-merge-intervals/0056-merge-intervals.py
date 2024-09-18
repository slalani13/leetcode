class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        i=0
        while i < len(intervals):
            start, end = intervals[i]
            while i < len(intervals) - 1 and intervals[i+1][0] >= start and intervals[i+1][0] <= end:
                end = max(end, intervals[i+1][1])
                i += 1
            output.append([start, end])
            i+=1
        return output