# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.output = [[]]
        self.l = []

    """
    def dfs(self, node, parent, node_type):
        if node.left == None and node.right == None:
            self.l.append(node.val)
            
            if node_type == "root":
                return True
            
            if node_type == "l":
                parent.left = None
                
            if node_type == "r":
                parent.right = None
                
        
        if node.left:
            self.dfs(node.left, node, "l")
            
        if node.right:
            self.dfs(node.right, node, "r")
    """
            
    def dfs_sol2(self, node):
        if node.left == None and node.right == None:
            self.output[0].append(node.val)
          
            
            return 0
        l = 0
        r = 0
        if node.left:
            l = self.dfs_sol2(node.left)
            
        if node.right:
            r = self.dfs_sol2(node.right)
            
        curr = max(l, r)+1
        if len(self.output) > curr:
            self.output[curr].append(node.val)
        else:
            self.output.append([node.val])
        
        return curr
            
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
    
        ## Solution 1 O(n^2)
        """
        while(True):
            self.l = []
            is_root = self.dfs(root, None, "root")
            self.output.append(self.l)
            #print(self.l)
            if is_root:
                break
        """
        
        ## Solution 1 O(n)
        self.dfs_sol2(root)    
        return self.output
                
        
        
            
        