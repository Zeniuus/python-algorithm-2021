from typing import List
from util import print_result


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            else:
                d[num] = i


print_result(Solution(),
             inputs=[[2, 7, 11, 15], 9],
             expected=[0, 1])
