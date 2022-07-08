"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def __init__(self):
        self.visited = {}
        
    def clone_node(self, node):
        
        if node == None:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        
        self.visited[node] = Node(node.val, None, None)
        return self.visited[node]

    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':    
        if head == None:
            return None
        
        node = head
        new_head = self.clone_node(head)
        new_head.random = self.clone_node(head.random)
        
        new_node = new_head
        
        
        while(True):
            
            if node.next == None:
                break 
            
            new_node.next = self.clone_node(node.next)
            new_node.next.random = self.clone_node(node.next.random)
            
            
            node = node.next
            new_node = new_node.next
            
        
      
        return new_head