from typing import List
from util import print_result


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            remaining_gas = 0
            count = 0
            start = i
            while count < len(gas) and remaining_gas >= 0:
                idx = i % len(gas)
                remaining_gas += gas[idx] - cost[idx]
                count += 1
                i += 1
            if count == len(gas) and remaining_gas >= 0:
                return start
        return -1


print_result(Solution(),
             inputs=[[1,2,3,4,5], [3,4,5,1,2]],
             expected=3)
print_result(Solution(),
             inputs=[[2,3,4], [3,4,3]],
             expected=-1)
