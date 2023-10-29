from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_productExceptSelf(self):
        solution = Solution()
        self.assertEqual(
            [24,12,8,6],
            solution.productExceptSelf(
                [1,2,3,4]
            )
        )
    def test2_longestConsecutive(self):
        solution = Solution()
        self.assertEqual(
            [0, 0, 9, 0, 0],
            solution.productExceptSelf(
                [-1,1,0,-3,3]
            )
        )
