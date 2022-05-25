# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        curr = None
        l1 = list1
        l2 = list2
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:  
            if list1.val <= list2.val:
                start = list1
                if list1.next == None:
                    start.next = list2
                    return start
                else:
                    l1 = list1.next    
            else:
                start = list2
                if list2.next == None:
                    start.next = list1
                    return start
                else:
                    l2 = list2.next
                    
            
        curr = start
        
        while True:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                if l1.next == None:
                    curr.next = l2
                    break
                else:
                    l1 = l1.next
                    
            else:
                curr.next = l2
                curr = curr.next
                if l2.next == None:
                    curr.next = l1
                    break
                else:
                    l2 = l2.next
                
                
        
        return start