from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_combinationSum2(self):
        solution = Solution()
        self.assertEqual(
            [
                [1, 1, 6],
                [1, 2, 5],
                [1, 7],
                [2, 6]
            ],
            solution.combinationSum2(
                [10, 1, 2, 7, 6, 1, 5],
                8
            )
        )

    def test2_combinationSum2(self):
        solution = Solution()
        self.assertEqual(
            [
                [1, 2, 2],
                [5]
            ],
        solution.combinationSum2(
                [2,5,2,1,2],
                5
            )
        )