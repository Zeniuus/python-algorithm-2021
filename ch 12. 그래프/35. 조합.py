from typing import List
from util import print_result


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def _combine(start: int, k: int) -> List[List[int]]:
            if k == 0:
                return [[]]

            result = []
            for first in range(start, n - (k - 1) + 1):
                temp = _combine(first + 1, k - 1)
                for c in temp:
                    c.insert(0, first)
                result += temp
            return result

        return _combine(1, k)


print_result(Solution(),
             inputs=[4, 2],
             expected=[
               [2,4],
               [3,4],
               [2,3],
               [1,2],
               [1,3],
               [1,4],
             ])
