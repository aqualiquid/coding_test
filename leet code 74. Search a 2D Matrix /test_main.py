from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_searchMatrix(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.searchMatrix(
                [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
                3
            )
        )

    def test2_searchMatrix(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.searchMatrix(
                [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
                13
            )
        )
