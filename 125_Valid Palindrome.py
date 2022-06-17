class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalnum()]
        start = 0
        end = len(s)-1
        is_palindrome = True
        
        if len(s)  <= 1:
            return is_palindrome
        
        while True:    
            if s[start] != s[end]:
                is_palindrome = False
                break
            else:
                if start == end or end-start == 1:
                    break
                
                start+=1
                end-=1
                    
        return is_palindrome