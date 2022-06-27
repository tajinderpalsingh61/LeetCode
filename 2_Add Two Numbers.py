# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        node1 = l1
        node2 = l2
        
        v1 = node1.val
        v2 = node2.val
        rem = 0
        
        while True:
            #print(v1, v2)
            v = rem+v1+v2
            if v >= 10:
                rem = int(v/10)
                v = v%10
            else:
                rem = 0
            
            out.append(v)
            
            if node1.next == None and node2.next == None:
                break
            
            if node1.next!=None:
                node1 = node1.next
                v1 = node1.val
            else:
                v1 = 0
                
            if node2.next!=None:
                node2 = node2.next
                v2 = node2.val
            else:
                v2 = 0
                
            
        
        if rem > 0:
            out.append(rem)
                
        
        #print(out)
        out_list = ListNode(out[0])
        curr = out_list
        for i in range(1, len(out)):
            temp = ListNode(out[i])
            curr.next = temp
            curr = curr.next
        
        return out_list