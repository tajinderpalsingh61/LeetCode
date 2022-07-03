# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    """
    reverse_link_list -> used in Solution 3 only
    """
    def reverse_link_list(self, head):
        
        if head == None:
            return None
        
        curr = head
        prev = None
        while(True):
            if curr.next != None: 
                new = curr.next
                curr.next = prev
                prev = curr
                curr = new
            
            else:
                curr.next = prev
                break
            
            
                
        return curr
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        l = []
        node = head
        
        while(True):            
            l.append(node.val)
            
            if node.next == None:
                break
                
            node = node.next
        """
            
        ## Solution 1
        """
        #return l == l[::-1]
        """
        
        ## OR
        """
        p1 = 0
        p2 = len(l)-1
        
        while(p1 < p2):
            if l[p1] != l[p2]:
                return False
            
            p1+=1
            p2-=1
            
        return True
        """
        
        ## Solution 2
        """
        self.fp = head
        
        def check_sub_palindrome(node):
            if node != None:
                if not check_sub_palindrome(node.next):
                    return False
                if self.fp.val != node.val:
                    return False
                
                self.fp = self.fp.next
            
            return True
            
        return check_sub_palindrome(head)            
        """
        
        ## Solution 3
        start = head
        node = head
        node2 = head
        rev = None
        while(True):
            reverse_start = False
            if node2.next == None or node2.next.next == None:
                rev = self.reverse_link_list(node.next)
                break
                
            node = node.next
            node2 = node2.next.next
            
        rev_node = rev
        front_node = head
        while(True):
            if rev_node == None:
                break
                
            if front_node.val != rev_node.val:
                return False
            
            rev_node = rev_node.next
            front_node =front_node.next
            
        return True