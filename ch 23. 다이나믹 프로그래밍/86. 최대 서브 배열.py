from typing import List
from util import print_result


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_cache = -9999999
        max_end_cache = -9999999
        for i in range(len(nums)):
            if i == 0:
                max_end_cache = nums[i]
                max_subarray_cache = nums[i]
            else:
                max_end_cache = max(nums[i], max_end_cache + nums[i])
                max_subarray_cache = max(max_subarray_cache, max_end_cache)
        return max_subarray_cache


print_result(Solution(),
             inputs=[[-2,1,-3,4,-1,2,1,-5,4]],
             expected=6)
print_result(Solution(),
             inputs=[[1]],
             expected=1)
print_result(Solution(),
             inputs=[[5,4,-1,7,8]],
             expected=23)
