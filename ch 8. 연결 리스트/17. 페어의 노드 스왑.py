from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, p, q = None, head, head.next
        new_head = q
        while True:
            if prev is not None:
                prev.next = q
            p.next = q.next
            q.next = p
            if p.next is None or p.next.next is None:
                break
            prev, p, q = p, p.next, p.next.next
        return new_head
