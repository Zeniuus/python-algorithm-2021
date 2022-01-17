from typing import List, Tuple
from util import print_result


class Solution():
    def solve(self, lines: List[str]) -> int:
        def parse_log_to_time_range(log: str) -> Tuple[int, int]:
            yyyyMMdd, HHmmssZZZ, duration = log.split(" ")
            yyyy, MM, dd = yyyyMMdd.split("-")
            HH, mm, ssZZZ = HHmmssZZZ.split(":")
            ss, ZZZ = ssZZZ.split(".")
            end_time_millis = ((((((((((int(yyyy) * 13) + int(MM)) * 32) + int(dd)) * 24) + int(HH)) * 60) + int(mm)) * 60) + int(ss)) * 1000 + int(ZZZ)

            start_time_millis = end_time_millis - int(float(duration.replace("s", "")) * 1000) + 1  # inclusive라 1ms 더해줌
            return start_time_millis, end_time_millis

        lines = [parse_log_to_time_range(line) for line in lines]
        count_elems = []
        for start_time_millis, end_time_millis in lines:
            count_elems.append((start_time_millis - 1000, 1))
            count_elems.append((end_time_millis, -1))
        count_elems.sort(key=lambda x: (x[0], -x[1]))  # count 증가와 감소 중 감소를 먼저 나오게 한다.

        result = 0
        curr = 0
        for time, count in count_elems:
            curr += count
            result = max(result, curr)

        return result


print_result(Solution(),
             inputs=[["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2.0s"]],
             expected=1)
print_result(Solution(),
             inputs=[["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2.0s"]],
             expected=2)
print_result(Solution(),
             inputs=[[
                 "2016-09-15 20:59:57.421 0.351s",
                 "2016-09-15 20:59:58.233 1.181s",
                 "2016-09-15 20:59:58.299 0.8s",
                 "2016-09-15 20:59:58.688 1.041s",
                 "2016-09-15 20:59:59.591 1.412s",
                 "2016-09-15 21:00:00.464 1.466s",
                 "2016-09-15 21:00:00.741 1.581s",
                 "2016-09-15 21:00:00.748 2.31s",
                 "2016-09-15 21:00:00.966 0.381s",
                 "2016-09-15 21:00:02.066 2.62s",
             ]],
             expected=7)
