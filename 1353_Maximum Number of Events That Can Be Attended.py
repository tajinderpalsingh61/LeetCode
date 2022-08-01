class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        heap = []
        
        n = max(events, key = lambda x: x[1])[1]
        cnt = 0
        j = 0
        for i in range(1, n+1):
            while(j<len(events) and i == events[j][0]):
                heappush(heap, events[j][1])
                j+=1
                
            while(heap and heap[0] < i):
                heappop(heap)
                
            if heap:
                heappop(heap)
                cnt+=1
                
        return cnt