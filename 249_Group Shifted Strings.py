class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict_key_string = {}
        
        def create_key_string(s):
            key_string = ""
            for i in range(1, len(s)):
                val = ord(s[i])-ord(s[i-1])
                val = val + 26 if val < 0 else val
                key_string += (str(val)+"#")
            
            #print(s, key_string)
                
            return key_string
        
        for s in strings:
            key_string = create_key_string(s)
            if key_string in dict_key_string:
                dict_key_string[key_string].append(s)
            else:
                dict_key_string[key_string] = [s]
            
                        
        out = []
        for l in dict_key_string:
            out.append(dict_key_string[l])
            
        return out
                