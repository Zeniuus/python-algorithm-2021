import collections
from typing import List
from util import print_result


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(lambda: [])
        for leaf, v in edges:
            graph[leaf].append(v)
            graph[v].append(leaf)
        leaves = collections.deque([v1 for v1, v2s in graph.items()
                                   if len(v2s) == 1])
        count = len(leaves)
        while count < n:
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for v in graph[leaf]:
                    graph[v].remove(leaf)
                    if len(graph[v]) == 1:
                        leaves.append(v)
                        count += 1
        return list(leaves)


print_result(Solution(),
             inputs=[4, [[1,0],[1,2],[1,3]]],
             expected=[1])
print_result(Solution(),
             inputs=[6, [[3,0],[3,1],[3,2],[3,4],[5,4]]],
             expected=[3, 4])
print_result(Solution(),
             inputs=[7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]],
             expected=[1, 2])
