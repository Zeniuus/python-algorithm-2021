from typing import List
from util import print_result


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]


print_result(Solution(),
             inputs=[[[1,3],[-2,2]], 1],
             expected=[[-2, 2]])
print_result(Solution(),
             inputs=[[[3,3],[5,-1],[-2,4]], 2],
             expected=[[3,3],[-2,4]])
