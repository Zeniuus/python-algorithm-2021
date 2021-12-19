from typing import List
from util import print_result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1
            left = nums[i]
            while j < k:
                middle = nums[j]
                right = nums[k]
                if left + middle + right == 0:
                    result.append([left, middle, right])
                    j += 1
                    while j < len(nums) and nums[j - 1] == nums[j]:
                        j += 1
                    k -= 1
                    while i < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif left + middle + right < 0:
                    j += 1
                    while j < len(nums) and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while i < k and nums[k + 1] == nums[k]:
                        k -= 1

        return result


print_result(Solution(),
             inputs=[[-1, 0, 1, 2, -1, -4]],
             expected=[[-1, -1, 2], [-1, 0, 1]])
print_result(Solution(),
             inputs=[[0]],
             expected=[])
