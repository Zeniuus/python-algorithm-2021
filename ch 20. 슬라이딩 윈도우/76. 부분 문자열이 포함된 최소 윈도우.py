import collections

from util import print_result


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, 0
        window_counter = collections.Counter()
        t_counter = collections.Counter(t)
        remaining_counter = collections.Counter(t)
        result = ""
        while j < len(s):
            window_counter[s[j]] += 1
            if s[j] in remaining_counter:
                remaining_counter[s[j]] -= 1
                if remaining_counter[s[j]] == 0:
                    del remaining_counter[s[j]]

            while not remaining_counter and i <= j:
                if result == "" or len(result) > j - i + 1:
                    result = s[i:j + 1]
                window_counter[s[i]] -= 1
                if window_counter[s[i]] < t_counter[s[i]]:
                    remaining_counter[s[i]] = 1
                i += 1
            j += 1
        return result


print_result(Solution(),
             inputs=["ADOBECODEBANC","ABC"],
             expected="BANC")
print_result(Solution(),
             inputs=["a", "a"],
             expected="a")
print_result(Solution(),
             inputs=[ "a", "aa"],
             expected="")
