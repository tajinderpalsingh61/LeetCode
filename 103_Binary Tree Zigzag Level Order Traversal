# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution: Traverse in BFS then while inserting reverse the list when lef = False

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = []
        output_list = []
        temp_list = []
        left = True
        prev_level = 0
        level = 1
        
        if root == None:
            return output_list
        else:
            queue.append((root, level))
            
        while(len(queue)>0):
            tup = queue.pop(0)
            node = tup[0]
            level = tup[1]
            
            if level != prev_level and len(temp_list) > 0:
                if left == False:
                    temp_list.reverse()
                                        
                output_list.append(temp_list)
                left = not left
                prev_level = level
                temp_list = [node.val]
            
            else:
                temp_list.append(node.val)
                
            if node.left != None:         
                queue.append((node.left, level+1))
            
            if node.right != None:
                queue.append((node.right, level+1))
                
        
        if(len(temp_list) > 0):
            if left == False:
                temp_list.reverse()
                                        
            output_list.append(temp_list)
            
                
                
        return output_list
                