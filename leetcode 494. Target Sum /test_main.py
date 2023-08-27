from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_findTargetSumWays(self):
        solution = Solution()
        self.assertEqual(
            5,
            solution.findTargetSumWays(
            [1,1,1,1,1],
            3
            )
        )

    def test2_findTargetSumWays(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.findTargetSumWays(
            [1],
            1
            )
        )
