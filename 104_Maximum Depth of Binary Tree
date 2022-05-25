# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 1

        if root == None:
            return 0
              
        
        def getMaxDepth(self, node, depth):
                if node.left == None and node.right == None:
                    if depth > self.max_depth:
                        self.max_depth = depth      

                if node.left != None:
                    getMaxDepth(self, node.left, depth+1)

                if node.right != None:
                    getMaxDepth(self, node.right, depth+1)
                
                
        getMaxDepth(self, root, 1) 
        return self.max_depth