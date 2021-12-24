import collections
from typing import List
from util import print_result


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(lambda: [])
        for time in times:
            edges[time[0]].append(time[1:])

        pending = collections.defaultdict(lambda: 1000000)
        for v, time in edges[k]:
            pending[v] = time
        finished = {k}
        result = 0

        while pending:
            min_v = -1
            for v, time in pending.items():
                if min_v == -1 or time < pending[min_v]:
                    min_v = v
            min_time = pending[min_v]

            finished.add(min_v)
            if result < min_time:
                result = min_time
            del pending[min_v]
            for v, time in edges[min_v]:
                if v not in finished:
                    pending[v] = min(pending[v], min_time + time)

        if len(finished) != n:
            return -1
        return result


print_result(Solution(),
             inputs=[[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
             expected=2)
print_result(Solution(),
             inputs=[[[1,2,1],[2,3,2],[1,3,2]], 3, 1],
             expected=2)
