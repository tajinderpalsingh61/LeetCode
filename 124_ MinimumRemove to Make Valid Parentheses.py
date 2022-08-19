class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid_string = []        
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                valid_string.append(s[i])
                stack.append(len(valid_string)-1)
            elif s[i] == ")":
                if len(stack) > 0:
                    valid_string.append(s[i])
                    stack.pop(-1)
            else:
                valid_string.append(s[i])
                
        
        # for i in range(len(stack)):
        #     del(valid_string[stack[i]-i])
        
        out = ""
        for i, c in enumerate(valid_string):
            if i not in stack:
                out+=c
            
                            
        return out