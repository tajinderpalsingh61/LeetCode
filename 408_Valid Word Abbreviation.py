class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr, abbr_ptr = 0, 0
        
        while word_ptr<len(word) and abbr_ptr<len(abbr):
            if abbr[abbr_ptr].isdigit():
                start = abbr_ptr
                
                if abbr[abbr_ptr] == "0":
                    return False
                
                val = 0
                while(start<len(abbr) and abbr[start].isdigit()):
                    val = val*10 + int(abbr[start])
                    start+=1
                    
                abbr_ptr=start
                word_ptr+=val
                
            else :
                if word[word_ptr]!=abbr[abbr_ptr]:
                    return False
                
                word_ptr+=1
                abbr_ptr+=1
                
        return word_ptr == len(word) and abbr_ptr == len(abbr)
