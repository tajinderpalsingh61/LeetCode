class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height)-1
        out = 0        
        
        while(s<e):
            temp = (e-s)*min([height[s], height[e]])
            if temp > out:
                out = temp
                
            if height[s] <= height[e]:
                s+=1
            else:
                e-=1
                
        return out