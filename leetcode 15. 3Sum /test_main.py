from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_threeSum(self):
        solution = Solution()
        self.assertEqual(
            [[-1, -1, 2], [-1, 0, 1]],
            solution.threeSum(
                [-1, 0, 1, 2, -1, -4]
            )
        )

    def test2_threeSum(self):
        solution = Solution()
        self.assertEqual(
            [],
            solution.threeSum(
                [0,1,1]
            )
        )
