from typing import List
from util import print_result


class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        result = 0
        while left < right:
            left_height, right_height = heights[left], heights[right]
            left_max = max(left_max, left_height)
            right_max = max(right_max, right_height)
            if left_max <= right_max:
                result += left_max - left_height
                left += 1
            else:
                result += right_max - right_height
                right -= 1

        return result


print_result(Solution(),
             inputs=[[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]],
             expected=6)
print_result(Solution(),
             inputs=[[4, 2, 3]],
             expected=1)
print_result(Solution(),
             inputs=[[4, 2, 0, 3, 2, 5]],
             expected=9)
print_result(Solution(),
             inputs=[[5, 4, 1, 2]],
             expected=1)
