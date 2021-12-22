import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        non_empty_lists = filter(lambda x: x, lists)
        heap = []
        for i, head in enumerate(non_empty_lists):
            heapq.heappush(heap, (head.val, i, head))

        result_head = ListNode(0, None)
        result_p = result_head
        while heap:
            val, i, p = heapq.heappop(heap)
            result_p.next = ListNode(val, None)
            result_p = result_p.next
            if p.next:
                heapq.heappush(heap, (p.next.val, i, p.next))

        return result_head.next
