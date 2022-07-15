# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head.next == None:
            return head
        
        def reverse(node):
            if node.next == None:
                return node
            
            start = node
            curr = node.next
            prev = node
            
            while(True):
                if curr.next == None:
                    curr.next = prev
                    start.next = None
                    break
                
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                                    
            
        left_node_prev = None
        left_node = None
        right_node = None
        right_node_next = None
        curr = head
        prev = None
        idx = 1
        
        while(True):                    
            if idx == left:
                left_node_prev = prev
                left_node= curr
                
            if idx == right:
                right_node= curr
                right_node_next = curr.next
                break
                
            prev = curr
            curr = curr.next
            idx+=1
    
        
        right_node.next = None                    
        reverse(left_node)
        
        if left_node_prev:
            left_node_prev.next = right_node
        else:
            head = right_node
        
        left_node.next = right_node_next
        return head