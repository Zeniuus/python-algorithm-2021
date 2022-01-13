import collections

from util import print_result


class Solution:
    def __init__(self):
        self.cache = collections.defaultdict()

    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if self.cache[n]:
            return self.cache[n]
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = result
        return result


print_result(Solution(),
             inputs=[2],
             expected=2)
print_result(Solution(),
             inputs=[3],
             expected=3)
