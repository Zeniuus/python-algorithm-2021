from typing import List
from util import print_result


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(0, len(nums) - 1):
            for j in range(len(nums) - 1, i, -1):
                if str(nums[j]) + str(nums[j - 1]) > str(nums[j - 1]) + str(nums[j]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return str(int(''.join([str(i) for i in nums])))



print_result(Solution(),
             inputs=[[10,2]],
             expected='210')
print_result(Solution(),
             inputs=[[3,30,34,5,9]],
             expected='9534330')
