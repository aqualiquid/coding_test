from typing import List
class Solutions:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])

        def counting_rows(start, end):
            if start> end:
                return False
            mid =(start+end)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return counting_cols(mid, )


            return 0

        def counting_cols(start, end):
            if start>end:
                return False
            mid = (start+end)//2


        return counting_rows(0, rows-1)
