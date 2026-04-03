# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        nl = ListNode()
        head = nl
        while l1 and l2:
            if l1.val < l2.val:
                nl.next = l1
                l1 = l1.next
            else:
                nl.next = l2
                l2 = l2.next
            nl = nl.next
        tmp = l1 if l1 else l2
        if tmp:
            while tmp:
                nl.next = tmp
                nl = nl.next
                tmp = tmp.next
        return head.next