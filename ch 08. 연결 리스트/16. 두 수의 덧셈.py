from typing import Optional
from util import print_result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_num(head: Optional[ListNode]):
            result = 0
            p = head
            digit = 1
            while p is not None:
                result += p.val * digit
                p = p.next
                digit *= 10
            return result

        n = linked_list_to_num(l1) + linked_list_to_num(l2)
        if n == 0:
            return ListNode(0, None)

        result = None
        last_node = None
        while n > 0:
            node = ListNode(n % 10, None)
            if result is None:
                result = node
                last_node = node
            else:
                last_node.next = node
                last_node = node
            n //= 10

        return result
