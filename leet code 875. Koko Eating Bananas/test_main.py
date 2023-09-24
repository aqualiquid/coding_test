from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_minEatingSpeed(self):
        solution = Solution()
        #piles = [3, 6, 7, 11], h = 8
        self.assertEqual(
            4,
            solution.minEatingSpeed(
                [3, 6, 7, 11],
                8
            )
        )

