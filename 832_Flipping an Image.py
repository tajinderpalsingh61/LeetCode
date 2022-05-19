class Solution:

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            p1 = 0
            p2 = n-1
            
            while True:
                if p1 == p2:
                    image[i][p1] = 0 if image[i][p1] == 1 else 1    
                    break
                    
                elif(p1 == p2-1):
                    temp = image[i][p1]
                    image[i][p1] = 0 if image[i][p2] == 1 else 1
                    image[i][p2] = 0 if temp == 1 else 1
                    break
                        
                else:
                    temp = image[i][p1]
                    image[i][p1] = 0 if image[i][p2] == 1 else 1
                    image[i][p2] = 0 if temp == 1 else 1
                    
                    # image[i][p1] = image[i][p2]
                    # image[i][p2] = temp

                    p1=p1+1
                    p2=p2-1
                
        return image