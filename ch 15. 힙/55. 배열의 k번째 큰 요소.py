import heapq
from typing import List
from util import print_result


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        return -heapq.nsmallest(k, heap)[k - 1]


print_result(Solution(),
             inputs=[[3,2,1,5,6,4], 2],
             expected=5)
print_result(Solution(),
             inputs=[[3,2,3,1,2,4,5,5,6], 4],
             expected=4)
