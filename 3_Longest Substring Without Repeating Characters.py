class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        
        out = 0
        i = 0
        while(i<len(s)):
            if s[i] in d.keys():
                temp = len(d.keys())
                i = d[s[i]]+1
                d = {}
                if temp > out:
                    out = temp
                    
            else:
                d[s[i]] = i
                i+=1
        
        temp = len(d)
        if temp > out:
            out = temp
        
        return out