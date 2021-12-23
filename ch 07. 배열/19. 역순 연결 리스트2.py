from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p_prev = None
        p = head
        for i in range(1, left):
            p_prev, p = p, p.next
        rev_before = p_prev
        rev_last = p

        for i in range(left, right + 1):
            p.next, p_prev, p = p_prev, p, p.next
        rev_start = p_prev
        rev_after = p

        if rev_before:
            rev_before.next = rev_start
        rev_last.next = rev_after

        if left == 1:
            head = p_prev

        return head
