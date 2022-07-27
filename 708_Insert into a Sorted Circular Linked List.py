"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        node = None
        new_node = Node(insertVal)
        
        if head is None:     
            new_node.next = new_node
            return new_node
        
        node = head
        prev = node
        node = node.next
        
        if prev == node:
            new_node.next = node
            node.next = new_node            
            return node
                
        
        while(True):
            if (new_node.val >= prev.val and new_node.val <= node.val):
                prev.next = new_node
                new_node.next = node
                break
                
            if prev.val > node.val:
                if new_node.val >= prev.val or new_node.val <= node.val:
                    prev.next = new_node
                    new_node.next = node
                    break
                               
            if node == head:
                prev.next = new_node
                new_node.next = node
                break
                
            prev = node
            node = node.next
                
        return head