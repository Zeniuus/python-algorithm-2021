from typing import List
from util import print_result


class Solution:
    def solve(self, n: int, arr1: List[int], arr2: List[int]) -> List[str]:
        def num_to_wall(num: int) -> str:
            result = ""
            for _ in range(n):
                if num % 2 == 1:
                    result = "#" + result
                else:
                    result = " " + result
                num = num // 2
            return result

        return [num_to_wall(a1 | a2) for a1, a2 in zip(arr1, arr2)]


print_result(Solution(),
             inputs=[5, [9,20,28,18,11], [30,1,21,17,28]],
             expected=["#####", "# # #", "### #", "#  ##", "#####"])
