from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_coin_change(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.change(
                5,
               [1,2,5]
            )
        )

    def test2_coin_change(self):
        solution = Solution()
        self.assertEqual(
            0,
            solution.change(
                3,
               [2]
            )
        )

    def test3_coin_change(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.change(
                10,
               [10]
            )
        )