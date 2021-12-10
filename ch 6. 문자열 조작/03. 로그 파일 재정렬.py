import re
from typing import List
from util import print_result


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        text_logs = [log for log in logs if not re.split(r' +', log, maxsplit=2)[1][0].isnumeric()]
        number_logs = [log for log in logs if re.split(r' +', log, maxsplit=2)[1][0].isnumeric()]

        def text_logs_comparator(log: str):
            identifier, data = log.split(' ', maxsplit=1)
            return data, identifier

        text_logs.sort(key=text_logs_comparator)

        return text_logs + number_logs


print_result(Solution(),
             inputs=[["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]],
             expected=["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
print_result(Solution(),
             inputs=[["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]],
             expected=["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])
