import collections
from typing import List
from util import print_result


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counts = [(v, k) for k, v in counter.items()]
        counts.sort()
        result = []
        for i in range(k):
            result.append(counts.pop()[1])

        return result


print_result(Solution(),
             inputs=[[1,1,1,2,2,3], 2],
             expected=[1,2])
