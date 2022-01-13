from typing import List
from util import print_result


class Solution:
    def rob(self, nums: List[int]) -> int:
        max_cache = []
        for i in range(len(nums)):
            if i == 0:
                max_cache.append(nums[0])
            elif i == 1:
                max_cache.append(max(nums[0], nums[1]))
            else:
                max_cache.append(max(max_cache[i - 2] + nums[i], max_cache[i - 1]))
        return max_cache[len(nums) - 1]


print_result(Solution(),
             inputs=[[1,2,3,1]],
             expected=4)
print_result(Solution(),
             inputs=[[2,7,9,3,1]],
             expected=12)
