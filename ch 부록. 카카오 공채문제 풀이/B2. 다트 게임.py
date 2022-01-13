import re
from util import print_result


class Solution:
    def solve(self, dart_result: str) -> int:
        def handle_multiplier(multiplier: str, score: int) -> int:
            exponential = 1
            if multiplier == "D":
                exponential = 2
            elif multiplier == "T":
                exponential = 3
            return score ** exponential

        def handle_option(option: str, score: int) -> int:
            if option == "*":
                return score * 2
            if option == "#":
                return -score
            return score

        matches = re.findall("(\\d+[SDT][*#]?)", dart_result)
        result = 0
        for i, match in enumerate(matches):
            score, multiplier, option = re.findall("(\\d+)([SDT])([*#]?)", match)[0]
            score = int(score)
            score = handle_multiplier(multiplier, score)
            score = handle_option(option, score)
            if i < len(matches) - 1 and "*" in matches[i + 1]:
                score *= 2
            result += score
        return result


print_result(Solution(),
             inputs=["1S2D*3T"],
             expected=37)
print_result(Solution(),
             inputs=["1D2S#10S"],
             expected=9)
print_result(Solution(),
             inputs=["1D2S0T"],
             expected=3)
print_result(Solution(),
             inputs=["1S*2T*3S"],
             expected=23)
print_result(Solution(),
             inputs=["1D#2S*3S"],
             expected=5)
print_result(Solution(),
             inputs=["1T2D3D#"],
             expected=-4)
print_result(Solution(),
             inputs=["1D2S3T*"],
             expected=59)
