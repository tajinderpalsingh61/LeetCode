class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Greedy Approach
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        out = 0
        compare = intervals[0]
        for i in range(1, len(intervals)):
            if (intervals[i][0] >= compare[0]) and (intervals[i][1] <= compare[1]):
                compare = intervals[i]
                out+=1
            elif (intervals[i][0] >= compare[0] and intervals[i][0] < compare[1]) and (intervals[i][1] > compare[1]):
                out+=1
            else:
                compare = intervals[i]
                
        return out