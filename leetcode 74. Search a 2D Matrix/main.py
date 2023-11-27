from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2
            reduced_mat = matrix[mid // cols][mid % cols]
            if reduced_mat == target:
                return True
            elif reduced_mat < target:
                left = mid +1
            elif reduced_mat > target:
                right = mid -1

        return False


