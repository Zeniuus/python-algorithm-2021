from typing import List
from util import print_result


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = [[False for _ in grid[0]] for _ in grid]

        result = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and not visited[i][j]:
                    mark_island_as_visited(grid, i, j, visited)
                    result += 1
                else:
                    visited[i][j] = True
        return result


def mark_island_as_visited(grid: List[List[str]], i: int, j: int, visited: List[List[bool]]):
    if grid[i][j] == '0' or visited[i][j]:
        return
    visited[i][j] = True
    height = len(grid)
    width = len(grid[0])
    if i > 0:
        mark_island_as_visited(grid, i - 1, j, visited)
    if j > 0:
        mark_island_as_visited(grid, i, j - 1, visited)
    if i < height - 1:
        mark_island_as_visited(grid, i + 1, j, visited)
    if j < width - 1:
        mark_island_as_visited(grid, i, j + 1, visited)


print_result(Solution(),
             inputs=[[
               ["1","1","1","1","0"],
               ["1","1","0","1","0"],
               ["1","1","0","0","0"],
               ["0","0","0","0","0"]
             ]],
             expected=1)
