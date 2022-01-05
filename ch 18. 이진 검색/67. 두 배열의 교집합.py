from typing import List
from util import print_result


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = set(nums2)
        return list(set([i for i in nums1 if i in nums2_set]))


print_result(Solution(),
             inputs=[[1,2,2,1], [2,2]],
             expected=[2])
print_result(Solution(),
             inputs=[[4,9,5], [9,4,9,8,4]],
             expected=[9,4])
