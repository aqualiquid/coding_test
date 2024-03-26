from unittest import TestCase
from main import Solution

class TestSolution(TestCase):

    def test1_isNStraightHand(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.isNStraightHand(
                [1,2,3,6,2,3,4,7,8],
                3
            )
        )

    def test2_isNStraightHand(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.isNStraightHand(
                [1,2,3,4,5],
                4
            )
        )