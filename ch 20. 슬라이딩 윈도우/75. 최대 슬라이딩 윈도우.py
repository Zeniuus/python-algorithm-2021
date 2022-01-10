import collections
import heapq
from typing import List
from util import print_result

# 내 풀이: O(n log k)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         heap = []
#         for i in range(k - 1):
#             heapq.heappush(heap, (-nums[i], i))
#
#         result = []
#         for i in range(k - 1, len(nums)):
#             heapq.heappush(heap, (-nums[i], i))
#             while True:
#                 (val, idx) = heap[0]
#                 if i - k + 1 <= idx:
#                     result.append(-val)
#                     break
#                 else:
#                     heapq.heappop(heap)
#         return result


# leetcode best 풀이: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx_deque = collections.deque()
        result = []
        for i in range(len(nums)):
            while idx_deque and idx_deque[0] < i - k + 1:
                idx_deque.popleft()
            while idx_deque and nums[idx_deque[-1]] < nums[i]:
                idx_deque.pop()
            idx_deque.append(i)
            if k - 1 <= i:
                result.append(nums[idx_deque[0]])
        return result



print_result(Solution(),
             inputs=[[1,3,-1,-3,5,3,6,7], 3],
             expected=[3,3,5,5,6,7])
print_result(Solution(),
             inputs=[[1], 1],
             expected=[1])
