from typing import List
from util import print_result


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result


print_result(Solution(),
             inputs=[[2,2,1]],
             expected=1)
print_result(Solution(),
             inputs=[[4,1,2,1,2]],
             expected=4)
