import collections

from util import print_result


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        i = 0
        result = 0
        max_char, max_char_count = None, 0
        for j in range(len(s)):
            counter[s[j]] += 1
            if max_char == s[j]:
                max_char_count += 1
            else:
                if counter[s[j]] > max_char_count:
                    max_char, max_char_count = s[j], counter[s[j]]
            while (j - i + 1) - max_char_count > k:
                counter[s[i]] -= 1
                if s[i] == max_char:
                    max_char, max_char_count = counter.most_common(1)[0]
                i += 1
            result = max(result, j - i + 1)
        return result


print_result(Solution(),
             inputs=["ABAB", 2],
             expected=4)
print_result(Solution(),
             inputs=[ "AABABBA", 1],
             expected=4)
