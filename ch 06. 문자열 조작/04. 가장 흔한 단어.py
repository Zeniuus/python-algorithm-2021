from collections import Counter
from typing import List
from util import print_result
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_counter = Counter()
        for word in re.split(r'[\W\s]+', paragraph):
            normalized_word = re.sub(r'[^\w]', '', word.lower())
            if normalized_word and normalized_word not in banned:
                word_counter[normalized_word] += 1

        return word_counter.most_common(1)[0][0]


print_result(Solution(),
             inputs=["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
             expected='ball')
print_result(Solution(),
             inputs=["a.", []],
             expected='a')
