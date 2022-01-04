import collections
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums)
        i = 0
        for color in range(3):
            for _ in range(counter[color]):
                nums[i] = color
                i += 1
