from typing import List

from util import print_result


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        result = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append(i)
        return result


print_result(Solution(),
             inputs=[[73,74,75,71,69,72,76,73]],
             expected=[1,1,4,2,1,1,0,0])