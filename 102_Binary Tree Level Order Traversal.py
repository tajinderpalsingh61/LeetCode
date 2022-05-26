# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = []
        out = []
        temp = []
        last_level = 0
        if root == None:
            return q
        else:
            q.append((root, 0))            
            
            while(len(q) > 0): 
                t = q.pop(0)
                node = t[0]
                l = t[1]
                
                if l != last_level:
                    out.append(temp)
                    temp = [node.val]
                else:
                    temp.append(node.val)
                                
                if node.left != None:
                    q.append((node.left, l+1))
                        
                if node.right != None:
                    q.append((node.right, l+1))
                
                last_level = l
                
            
            if len(temp) > 0:
                out.append(temp)
                
                    
        return out    