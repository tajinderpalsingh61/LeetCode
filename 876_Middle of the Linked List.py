# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Two pointer approach
        node = head.next
        if node == None:
            return head
        elif node.next == None:
            return node
        else:
            node2 = node.next
            
        while True:
            if node2.next == None:
                return node
            else:
                node = node.next
                node2=node2.next
                
                if node2.next == None:
                    return node
                else:
                    node2=node2.next