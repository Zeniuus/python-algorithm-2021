from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd, even = head, head.next
        even_head = even
        while True:
            next_odd = even.next if even is not None else None
            next_even = next_odd.next if next_odd is not None else None

            odd.next = next_odd
            if even is not None:
                even.next = next_even

            if next_odd is None:
                break
            odd, even = next_odd, next_even

        odd.next = even_head
        return head

