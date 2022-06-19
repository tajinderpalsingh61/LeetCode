class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        out_list = []
        
        for q in queries:
            status = True
            j=0
            for i, c in enumerate(q):
                if j<len(pattern) and c == pattern[j]:
                    j+=1
                else:
                    if c.islower():
                        continue
                    else:
                        status = False
            
            if j < len(pattern):
                status = False
            
            out_list.append(status)
            
        
        return out_list