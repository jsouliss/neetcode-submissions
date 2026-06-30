"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        newHead = ListNode() 
        newTail = newHead

        while head1 and head2:
            if head1.val < head2.val:
                newTail.next = head1
                newTail = head1
                head1 = head1.next
            else:
                newTail.next = head2
                newTail = head2
                head2 = head2.next
        if head1:
            newTail.next = head1
        else:
            newTail.next = head2
        return newHead.next