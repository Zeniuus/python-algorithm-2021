from util import print_result


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            c_idx = s.index(c)
            suffix = s[c_idx:]
            if set(s) == set(suffix):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''


print_result(Solution(),
             inputs=['bcabc'],
             expected='abc')
