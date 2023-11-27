from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_coinChange(self):
        solution = Solution()
        self.assertEqual(
            3,
            solution.coinChange(
                [1, 2, 5],
                11
            )
        )

    def test2_coinChange(self):
        solution = Solution()
        self.assertEqual(
            -1,
            solution.coinChange(
                [2],
                3)
        )

    def test3_coinChange(self):
        solution = Solution()
        self.assertEqual(
            0,
            solution.coinChange(
                [1],
                0)
        )