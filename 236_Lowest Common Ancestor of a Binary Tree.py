# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dict_parent = {}
        
        def traverse(node, parent):
            dict_parent[node] = parent
            
            if node.left:
                traverse(node.left, node)
                
            if node.right:
                traverse(node.right, node)
                
        traverse(root, None)
        
        list_parent = []
        list_parent.append(p.val)
        list_parent.append(q.val)
        
        while(True):
            if dict_parent[p]:
                parent = dict_parent[p]
                if parent.val in list_parent:
                    return parent
                else:
                    list_parent.append(parent.val)
                    p = parent
                    
            if dict_parent[q]:
                parent = dict_parent[q]
                if parent.val in list_parent:
                    return parent
                else:
                    list_parent.append(parent.val)
                    q = parent    