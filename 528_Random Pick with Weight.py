import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cum = []
        t = 0
        for x in self.w:
            t+=x
            self.cum.append(t)
        self.total = t
        
    def pickIndex(self) -> int:
        target = random.random()*self.total
        
        # Solution 1
        # for i, x in enumerate(self.cum):
        #     if target<x:
        #         return i
        
        # Solution 2
        low, high = 0, len(self.cum)
        while(low<high):
            mid = low + (high-low)//2
            if target > self.cum[mid]:
                low = mid+1
            else:
                high = mid
            
        return low
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()