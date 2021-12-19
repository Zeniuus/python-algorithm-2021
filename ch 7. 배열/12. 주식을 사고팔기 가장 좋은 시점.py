from typing import List
from util import print_result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 9999999
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


print_result(Solution(),
             inputs=[[7,1,5,3,6,4]],
             expected=5)
print_result(Solution(),
             inputs=[[7,6,4,3,1]],
             expected=0)