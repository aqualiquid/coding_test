from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_cnt = 0

        # initilize the queue w/ al rotten orranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        # directions for the 4 neighbors cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inc_min = 0

        # BFS
        while queue and fresh_cnt > 0:
            inc_min +=1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0<=nx <rows and 0<=ny <cols and \
                        grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_cnt -= 1
        return inc_min if fresh_cnt == 0 else -1
