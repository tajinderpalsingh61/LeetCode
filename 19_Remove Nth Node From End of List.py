# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                    
        #Solution 1
        """
        def get_node_cnt(curr):
            cnt = 0    
            while(True):
                if curr == None:
                    return cnt      
                curr = curr.next
                cnt+=1
           
        cnt = get_node_cnt(head)
        
        # Single Node
        if cnt == 1:
            return None
        
        node_to_remove = cnt+1-n
        
        if node_to_remove == 1:
            head = head.next
        
        prev = head
        curr = head
    
        while(True):
            if node_to_remove == 1:
                prev.next = curr.next
                return head
            
            prev = curr
            curr = curr.next
            node_to_remove-=1
        
        return head
        """
       
        # Solution 2
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n+1):
            first = first.next

        while(True):
            if first == None:
                second.next = second.next.next
                break

            first = first.next
            second = second.next

        return dummy.next