from typing import List, Tuple
from util import print_result


# 내 풀이: O(log mn) = O(log m + log n)?? -> 근데 360ms이나 걸린다...
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def search_matrix(start: Tuple[int, int], end: Tuple[int, int]) -> bool:
#             mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
#             if start[0] > end[0] or start[1] > end[1]:
#                 return False
#             if matrix[mid[0]][mid[1]] == target:
#                 return True
#             elif matrix[mid[0]][mid[1]] < target:
#                 return search_matrix((mid[0] + 1, start[1]), (end[0], mid[1])) \
#                        or search_matrix((start[0], mid[1] + 1), (mid[0], end[1])) \
#                        or search_matrix((mid[0] + 1, mid[1] + 1), end)
#             else:
#                 return search_matrix((mid[0], start[1]), (end[0], mid[1] - 1)) \
#                        or search_matrix((start[0], mid[1]), (mid[0] - 1, end[1])) \
#                        or search_matrix(start, (mid[0] - 1, mid[1] -1))
#
#         return search_matrix((0, 0), (len(matrix) - 1, len(matrix[0]) - 1))
# 책 풀이: O(m + n)? -> 근데 160ms 밖에 안 걸린다...
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


print_result(Solution(),
             inputs=[[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5],
             expected=True)
print_result(Solution(),
             inputs=[[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20],
             expected=False)
print_result(Solution(),
             inputs=[[[1],[2],[3],[4],[5]], 5],
             expected=True)