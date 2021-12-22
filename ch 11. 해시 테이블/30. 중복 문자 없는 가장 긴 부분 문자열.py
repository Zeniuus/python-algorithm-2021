import collections
from util import print_result


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        counter = collections.Counter()
        i = 0
        result = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            result = max(result, j - i + 1)

        return result


print_result(Solution(),
             inputs=['abcabcbb'],
             expected=3)
