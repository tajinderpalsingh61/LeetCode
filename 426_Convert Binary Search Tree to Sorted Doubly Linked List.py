"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""



class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        if root == None:
            return None
        
        def traversal(node):
           
            l = None
            r = None
            
            if node.left != None:
                l = traversal(node.left)
                
            if node.right != None:
                r = traversal(node.right)
                
            s= None
            e = None
            if l != None:
                node.left = l[1]
                l[1].right = node
                s = l[0]
            else:
                s = node
                
            if r != None:
                node.right = r[0]
                r[0].left = node
                e = r[1]
            else:
                e = node
                  
            return (s, e)
                
        
        (start, end) = traversal(root)
        start.left = end
        end.right = start
        
        return start
            
                
            
        