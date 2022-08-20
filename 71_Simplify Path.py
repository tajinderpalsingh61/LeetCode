class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        #print(path)
        out = []
        
        for x in path:
            if x == "" or x == ".":
                pass
            elif x == "..":
                if len(out) >= 1:
                    out.pop(-1)
            else:
                out.append(x)
                
        out = "/".join(out)
        return "/"+out