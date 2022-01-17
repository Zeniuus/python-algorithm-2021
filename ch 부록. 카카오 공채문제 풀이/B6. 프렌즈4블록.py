from typing import List
from util import print_result


class Solution():
    def solve(self, m: int, n: int, board: List[str]) -> int:
        deleted_marker = " "
        result = 0
        new_board = [[c for c in line] for line in board]

        def delete() -> bool:
            nonlocal result
            deleting_indexes = []
            for i in range(1, m):
                for j in range(n - 1):
                    if new_board[i][j] != deleted_marker \
                            and new_board[i - 1][j] == new_board[i][j] \
                            and new_board[i - 1][j + 1] == new_board[i][j] \
                            and new_board[i][j + 1] == new_board[i][j]:
                        deleting_indexes.append((i, j))
            for i, j in deleting_indexes:
                for k in range(2):
                    for l in range(2):
                        if new_board[i - k][j + l] != deleted_marker:
                            new_board[i - k][j + l] = deleted_marker
                            result += 1
            return len(deleting_indexes) > 0

        def pull_down():
            for j in range(n):
                new_column = []
                deleted_count = 0
                for i in range(m - 1, -1, -1):
                    if new_board[i][j] != deleted_marker:
                        new_column.append(new_board[i][j])
                    else:
                        deleted_count += 1
                for _ in range(deleted_count):
                    new_column.append(deleted_marker)
                for i in range(m - 1, -1, -1):
                    new_board[i][j] = new_column[m - 1 - i]

        while delete():
            pull_down()
        return result


print_result(Solution(),
             inputs=[4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
             expected=14)
print_result(Solution(),
             inputs=[6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]],
             expected=15)
