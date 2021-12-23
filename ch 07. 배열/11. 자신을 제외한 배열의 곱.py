from typing import List
from util import print_result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(result[i - 1] * nums[i])

        acc_product = 1
        for i in range(len(nums) - 1, 0, -1):
            result[i] = result[i - 1] * acc_product
            acc_product *= nums[i]

        result[0] = acc_product

        return result


print_result(Solution(),
             inputs=[[1, 2, 3, 4]],
             expected=[24, 12, 8, 6])
print_result(Solution(),
             inputs=[[-1, 1, 0, -3, 3]],
             expected=[0, 0, 9, 0, 0])