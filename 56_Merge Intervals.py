class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(intervals)
        
        if len(intervals) == 1:
            return intervals
        
        prev = None
        curr = None
        out = []
        for x in intervals:
            if len(out) > 0:
                prev = out[len(out)-1]
                if x[0] <= prev[1]:
                    out[len(out)-1] = [prev[0], max(prev[1], x[1])]
                else:
                    out.append(x)
            else:
                out.append(x)
                                
        return out