class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        min_val = 9999
        
        for x in prices:
            if x < min_val:
                min_val = x
                
            if x-min_val > out:
                out = x-min_val
                    
        return out