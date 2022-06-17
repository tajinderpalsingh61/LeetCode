class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        
        out = list(palindrome)
        for i in range(math.floor(len(palindrome)/2)):
            if out[i] != "a":
                out[i] = "a"
                return "".join(out)
            
        out[len(out)-1] = "b"
        return "".join(out)