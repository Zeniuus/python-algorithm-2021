import collections
from typing import List
from util import print_result


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * num_courses
        graph = collections.defaultdict(lambda: [])
        for prerequisite in prerequisites:
            if prerequisite[0] == prerequisite[1]:
                return False
            graph[prerequisite[1]].append(prerequisite[0])

        route = set()

        def detect_cycle(curr: int):
            if curr in route:
                return True
            if visited[curr]:
                return False

            visited[curr] = True
            children = graph[curr]
            route.add(curr)
            for child in children:
                if detect_cycle(child):
                    return True
            route.remove(curr)
            return False

        for curr in range(num_courses):
            if detect_cycle(curr):
                return False
        return True


print_result(Solution(),
             inputs=[20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]],
             expected=False)
print_result(Solution(),
             inputs=[3, [[0,2],[1,2],[2,0]]],
             expected=False)
