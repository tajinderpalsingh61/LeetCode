# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next == None:
            return head
        else:
            node = head.next
            prev = head
            head.next = None
            while True:
                if node.next == None:
                    node.next = prev
                    return node
                else:
                    temp = node.next
                    node.next = prev
                    prev = node
                    node = temp
        