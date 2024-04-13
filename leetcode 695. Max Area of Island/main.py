from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       # Graph problem, Depth First Search (DFS) utilize
        if not grid :
            return 0
        def dfs(row, col):
            # if the current ptr exceeds the grid (i.e., out of the index)
            if row <0 or row >= len(grid) or col<0 or col >= len(grid[0]) \
            or grid[row][col] ==0:
                return 0
            grid[row][col] = 0
            area = 1
            area += dfs(row+1, col)
            area += dfs(row, col+1)
            area += dfs(row-1, col)
            area += dfs(row, col-1)
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    max_area = max(max_area, dfs(row,col))
        return max_area
