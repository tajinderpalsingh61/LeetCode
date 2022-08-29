# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        out = []
        node = None
        if root:
            queue.append((root, 0))
            last = (root, 0)
        
        while(len(queue) > 0):   
            node, level = queue.pop(0)
            last_node, last_level = last
            if last_level < level:
                out.append(last_node.val)
            last = (node, level)
            
            if node.left:                
                queue.append((node.left, level+1))
            
            if node.right:
                last = (node, level)
                queue.append((node.right, level+1))
        
        if node:
            out.append(node.val)
            return out
                
                
            