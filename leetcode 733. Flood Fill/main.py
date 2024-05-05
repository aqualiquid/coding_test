from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        current_color = image[sr][sc]
        if current_color == color:
            return image

        def dfs(r, c):
            if image[r][c] == current_color:
                image[r][c] = color
                if r >= 1:
                    dfs(r - 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image