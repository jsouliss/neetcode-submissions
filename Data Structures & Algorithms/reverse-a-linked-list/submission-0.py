# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
    
        current = head
        prev = None
        next = None
        
        # Traverse to end of List
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head 