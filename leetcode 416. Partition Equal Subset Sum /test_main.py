from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_canPartition(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.canPartition(
            [1, 5, 11, 5]
            )
        )

    def test2_canPartition(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.canPartition(
            [1, 2, 3, 5]
            )
        )
