class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            s = "".join(sorted(x))
            if s in d.keys():
                d[s].append(x)
            else:
                d[s] = [x]
                
        out = [x for x in d.values()]
        return out 