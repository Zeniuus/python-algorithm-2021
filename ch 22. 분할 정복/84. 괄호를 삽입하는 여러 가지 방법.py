from typing import List
from util import print_result


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        tokens = []
        number_start = 0
        for i, c in enumerate(expression):
            if c in '+*-':
                tokens.append(expression[number_start:i])
                tokens.append(c)
                number_start = i + 1
        tokens.append(expression[number_start:])
        return _diff_ways_to_compute(tokens)


def _diff_ways_to_compute(tokens: List[str or int]) -> List[int]:
    if len(tokens) <= 1:
        return tokens

    result = []
    for i in range(len(tokens) // 2):
        operator_idx = 2 * i + 1
        partial_result1 = _diff_ways_to_compute(tokens[:operator_idx])
        partial_result2 = _diff_ways_to_compute(tokens[operator_idx + 1:])
        result += [handle_operator(tokens[operator_idx], n1, n2) for n1 in partial_result1 for n2 in partial_result2]
    return result


def handle_operator(operator: str, n1: str or int, n2: str or int) -> int:
    if operator == '+':
        return int(n1) + int(n2)
    if operator == '*':
        return int(n1) * int(n2)
    return int(n1) - int(n2)


print_result(Solution(),
             inputs=["2-1-1"],
             expected=[0,2])
print_result(Solution(),
             inputs=["2*3-4*5"],
             expected=[-34,-14,-10,-10,10])
