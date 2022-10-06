class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)-1
        l2 = len(num2)-1
        
        carry = 0
        out = ""
        while(l1>=0 or l2>=0):
            #print(l1, l2)
            d1 = ord(num1[l1]) - ord('0') if l1>=0 else 0
            d2 = ord(num2[l2]) - ord('0') if l2>=0 else 0
            
            #print(d1, d2)
            val = (d1+d2+carry)%10
            carry = (d1+d2+carry)//10
            out+=str(val)
            
            l1-=1
            l2-=1
            
        if carry > 0:
            out+=str(carry)
            
        #print(out)
        return out[::-1]