from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_maximum_prdudct_subarray(self):
        solution = Solution()
        self.assertEqual(
            6,
            solution.maxProduct(
                [2,3,-2,4]
            )
        )

    def test2_maximum_prdudct_subarray(self):
        solution = Solution()
        self.assertEqual(
            0,
            solution.maxProduct(
                [-2, 0, -1]
            )
        )
