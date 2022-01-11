import collections
from typing import List
from util import print_result


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown_tasks = collections.deque()
        counter = [(count, task) for task, count in collections.Counter(tasks).items()]
        counter.sort()
        remaining_task_count = len(tasks)
        result = 0
        while remaining_task_count > 0:
            if counter:
                count, task = counter.pop()
                cooldown_tasks.append((count - 1, task))
                remaining_task_count -= 1
            else:
                cooldown_tasks.append((None, 0))

            if len(cooldown_tasks) > n:
                count, task = cooldown_tasks.popleft()
                if task and count:
                    idx = len(counter)
                    while idx - 1 >= 0 and counter[idx - 1][0] > count:
                        idx -= 1
                    counter.insert(idx, (count, task))

            result += 1

        return result


print_result(Solution(),
             inputs=[["A","A","A","B","B","B"], 2],
             expected=8)
print_result(Solution(),
             inputs=[["A","A","A","B","B","B"], 0],
             expected=6)
print_result(Solution(),
             inputs=[["A","A","A","A","A","A","B","C","D","E","F","G"], 2],
             expected=16)
