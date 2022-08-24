class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #Brute Force
        """
        out = 1
        if n < 0:
            x = 1/x
            n = -1*n
            
        for i in range(n):
            out*=x
            
        return out
        """
        
        #recursive approach Divide and Conquer
        """
        if x == 0:
            return 0
        
        self.out = 1
        if n < 0:
            x = 1/x
            n = -1*n
            
        def calc_pow(n):
            if n == 0:
                return 1
            else:
                if n == 1:
                    self.out*=x
                    return self.out
                elif n%2 == 0:
                    out = calc_pow(n//2)
                    return out*out
                else:
                    out = calc_pow(n//2)
                    return out*out*x
                    
        return calc_pow(n)
        """
        
        #SC: O(1)
        if x == 0:
            return 0
        
        if n < 0:
            x = 1/x
            n = -1*n
            
        
        out = 1
        while(n>0):
            #print(n)
            if n%2 == 0:
                x = x*x
                n = n//2
                
            elif n%2 == 1:
                out = out*x
                n = n-1
                
            else:
                pass
            
            #print("==="+str(out))
            
        return out
                
                
        