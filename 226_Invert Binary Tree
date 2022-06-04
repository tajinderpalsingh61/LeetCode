# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
              
        node = None
        if root == None:
            return None
        else:
            node = root
            
        
        def invert(node):
            if node.left == None and node.right == None:
                return node
            else:   
                temp = node.left
                node.left = node.right
                node.right = temp
                
                if node.left != None:
                    invert(node.left)
                if node.right != None:
                    invert(node.right)
                
        
        invert(node)
        return root
        