from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_maxArea(self):
        solution = Solution()
        self.assertEqual(
            49,
            solution.maxArea(
                [1,8,6,2,5,4,8,3,7]
            )
        )
    def test2_maxArea(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.maxArea(
                [1,1]
            )
        )