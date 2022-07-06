# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.level_dict = {}
        self.min_level = 999
        self.max_level = -999
        
        
        self.dd = defaultdict(list)
    
    def add_level_dict(self, node, level):
        if level in self.level_dict:
            self.level_dict[level].append(node)
        else:
            self.level_dict[level] = [node]
            
        if level < self.min_level:
            self.min_level = level
            
        if level > self.max_level:
            self.max_level = level
    
    def bfs(self, root, level):
        queue = []     
        
        if root == None:
            return None
        
        queue.append((root, level))
        while(len(queue) > 0):
            node, level = queue.pop(0)
            self.add_level_dict(node, level)
            
            if node.left !=None:
                queue.append((node.left, level-1))
                
            if node.right !=None:
                queue.append((node.right, level+1))
                
                
    def dfs(self, node, row, column):
        if node == None:
            return
        
        self.dd[column].append((row, node))
        self.min_level = min(self.min_level, column)
        self.max_level = max(self.max_level, column)
        
        if node.left != None:
            self.dfs(node.left, row+1, column-1)
            
        if node.right != None:
            self.dfs(node.right, row+1, column+1)
            
  
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        output_list = []
        
        ## Solution 1
        """
        self.bfs(root, 0)
        for i in range(self.min_level, self.max_level+1):
            j = len(output_list)
            output_list.append([])
            for x in self.level_dict[i]:
                output_list[j].append(x.val)
        """
        
        ## Solution 2
        
        self.dfs(root, 0, 0)
        for i in range(self.min_level, self.max_level+1):
            self.dd[i].sort(key= lambda x: x[0])
            t = [x[1].val for x in self.dd[i]]
            output_list.append(t)
        
        return output_list