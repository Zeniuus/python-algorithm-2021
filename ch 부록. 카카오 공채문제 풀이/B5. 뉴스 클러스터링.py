import collections

from util import print_result


class Solution():
    def solve(self, str1: str, str2: str) -> int:
        total_count = 0

        def get_counter(s: str):
            nonlocal total_count
            counter = collections.Counter()
            for i in range(len(s) - 1):
                word = s[i:i + 2]
                if word.isalpha():
                    counter[word.lower()] += 1
                    total_count += 1
            return counter

        counter1 = get_counter(str1)
        counter2 = get_counter(str2)
        if not counter1 and not counter2:
            return 65536

        intersect_count = 0
        for k in counter1.keys():
            intersect_count += min(counter1[k], counter2[k])
        union_count = total_count - intersect_count
        return intersect_count * 65536 // union_count



print_result(Solution(),
             inputs=["FRANCE", "french"],
             expected=16384)
print_result(Solution(),
             inputs=["handshake", "shake hands"],
             expected=65536)
print_result(Solution(),
             inputs=["aa1+aa2", "AAAA12"],
             expected=43690)
print_result(Solution(),
             inputs=["E=M*C^2", "e=m*c^2"],
             expected=65536)
