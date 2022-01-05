from typing import List
from util import print_result


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotated_idx = 0
        first, last = 0, len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[first] <= nums[last]:
                rotated_idx = first
                break

            if nums[mid] > nums[last]:
                if nums[mid + 1] < nums[last]:
                    rotated_idx = mid + 1
                    break
                first = mid + 1
                continue
            else:
                last = mid
                continue

        def binary_search(arr: List[int], first: int, last: int) -> int:
            if first > last:
                return -1
            mid = (first + last) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binary_search(arr, first, mid - 1)
            else:
                return binary_search(arr, mid + 1, last)

        result1 = binary_search(nums, 0, rotated_idx - 1)
        result2 = binary_search(nums, rotated_idx, len(nums) - 1)
        if result1 >= 0:
            return result1
        elif result2 >= 0:
            return result2
        else:
            return -1


print_result(Solution(),
             inputs=[[4,5,6,7,0,1,2], 0],
             expected=4)
print_result(Solution(),
             inputs=[[4,5,6,7,0,1,2], 3],
             expected=-1)
print_result(Solution(),
             inputs=[[3,1], 1],
             expected=1)
