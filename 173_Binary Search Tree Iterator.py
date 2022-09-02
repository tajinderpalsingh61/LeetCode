# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # Approach 1
    """
    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.index = -1
        self._inorderTraversal(root)

    def _inorderTraversal(self, root):
        node = root
        if not node:
            return
        
        if node.left:
            self._inorderTraversal(node.left)                

        self.nodes.append(node.val)

        if node.right:
            self._inorderTraversal(node.right)
            
    
    def next(self) -> int:
        self.index+=1
        return self.nodes[self.index]                

    def hasNext(self) -> bool:
        return self.index+1 < len(self.nodes)
    """
    
    # Approach 2 Stack appraoch
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.index = -1
        self._leftTraversal(root)

    def _leftTraversal(self, root):
        node = root
        while node:
            self.stack.append(node)
            node = node.left            
    
    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self._leftTraversal(top.right)
            
        return top.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()