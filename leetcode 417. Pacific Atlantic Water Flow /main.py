from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reach = set()
        atlantic_reach = set()

        def dfs(r, c, reach, prev_height):
            if ((r, c) in reach or r < 0 or r >= m or c < 0 or c >= n or \
                    heights[r][c] < prev_height):
                return
            reach.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reach, heights[r][c])

        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])

        return [[r, c] for r, c in (pacific_reach & atlantic_reach)]
