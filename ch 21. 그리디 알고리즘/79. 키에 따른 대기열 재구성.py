import heapq
from typing import List
from util import print_result


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result


print_result(Solution(),
             inputs=[[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]],
             expected=[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])
print_result(Solution(),
             inputs=[[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]],
             expected=[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]])
