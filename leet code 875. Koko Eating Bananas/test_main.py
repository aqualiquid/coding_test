from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_minEatingSpeed(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.minEatingSpeed(
                [3, 6, 7, 11],
                8
            )
        )
    def test2_minEatingSpeed(self):
        solution = Solution()
        self.assertEqual(
            30,
            solution.minEatingSpeed(
                [30,11,23,4,20],
                5
            )
        )
    def test3_minEatingSpeed(self):
        solution = Solution()
        self.assertEqual(
            23,
            solution.minEatingSpeed(
                [30,11,23,4,20],
                6
            )
        )