class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        s = 0
        for i in nums:
            s = s+i
            if s < min_val:
                min_val = s
                
        return min_val*-1+1               