from typing import List
from collections import defaultdict

from util import print_result


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(lambda: [])
        for s in strs:
            sorted_s = "".join(sorted(s))
            map[sorted_s].append(s)
        return [v for k, v in map.items()]


print_result(Solution(),
             inputs=[["eat","tea","tan","ate","nat","bat"]],
             expected=[["bat"],["nat","tan"],["ate","eat","tea"]])
print_result(Solution(),
             inputs=[['']],
             expected=[['']])
