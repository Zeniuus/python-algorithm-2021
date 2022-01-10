from util import print_result


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return (a ^ b) + ((a & b) << 1)


print_result(Solution(),
             inputs=[1, 2],
             expected=3)
print_result(Solution(),
             inputs=[3, 3],
             expected=6)
print_result(Solution(),
             inputs=[-1, -2],
             expected=-3)
print_result(Solution(),
             inputs=[1, -2],
             expected=-1)