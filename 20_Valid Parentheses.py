class Solution:
    def isValid(self, s: str) -> bool:
        
        dict_brackets = {'(': ')',
                         '{': '}',
                         '[': ']'
                        }

        if len(s) == 1:
            return False
        
        stack = []
        
        for b in s:
            if b in dict_brackets.keys():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                
                o = stack.pop(-1)
                if dict_brackets[o] == b:
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False