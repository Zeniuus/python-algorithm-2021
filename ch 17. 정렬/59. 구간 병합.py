from typing import List

from util import print_result


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i + 1 < len(intervals):
            start_1, end_1 = intervals[i]
            start_2, end_2 = intervals[i + 1]
            if start_2 <= end_1:
                intervals.pop(i)
                intervals[i] = [start_1, max(end_1, end_2)]
            else:
                i += 1
        return intervals


print_result(Solution(),
             inputs=[[[1,3],[2,6],[8,10],[15,18]]],
             expected=[[1,6],[8,10],[15,18]])
print_result(Solution(),
             inputs=[[[1,4],[4,5]]],
             expected=[[1,5]])
print_result(Solution(),
             inputs=[[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]],
             expected=[[1,3],[4,7]])
