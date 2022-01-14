import re
from typing import List
from util import print_result


class Solution():
    def solve(self, n: int, t: int, m: int, timetable: List[str]) -> str:
        def str_time_to_minutes(time: str) -> int:
            hour, minute = re.findall("(\\d\\d):(\\d\\d)", time)[0]
            return int(hour) * 60 + int(minute)

        timetable = sorted([str_time_to_minutes(time) for time in timetable])
        next_crew_idx = 0
        shuttle_time = 9 * 60 - t
        last_crew_time = 24 * 60
        for _ in range(n):
            shuttle_time += t
            for _ in range(m):
                if next_crew_idx < len(timetable) and timetable[next_crew_idx] <= shuttle_time:
                    last_crew_time = timetable[next_crew_idx]
                    next_crew_idx += 1
                else:
                    last_crew_time = 24 * 60
                    break

        last_time = min(9 * 60 + t * (n - 1), last_crew_time - 1)
        hour = str(last_time // 60)
        if len(hour) == 1:
            hour = f'0{hour}'
        minute = str(last_time % 60)
        if len(minute) == 1:
            minute = f'0{minute}'
        return f'{hour}:{minute}'


print_result(Solution(),
             inputs=[1, 1, 5, ["08:00","08:01","08:02","08:03"]],
             expected="09:00")
print_result(Solution(),
             inputs=[2, 10, 2, ["09:10","09:09","08:00"]],
             expected="09:09")
print_result(Solution(),
             inputs=[2, 1, 2, ["09:00","09:00","09:00","09:00"]],
             expected="08:59")
print_result(Solution(),
             inputs=[1, 1, 5, ["00:01","00:01","00:01","00:01","00:01"]],
             expected="00:00")
print_result(Solution(),
             inputs=[1, 1, 1, ["23:59"]],
             expected="09:00")
print_result(Solution(),
             inputs=[10, 60, 45, ["23:59" for _ in range(16)]],
             expected="18:00")
