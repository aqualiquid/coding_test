from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_twoSum(self):
        solution = Solution()
        self.assertEqual(
            {0,1},
            solution.twoSum(
                [2, 7, 11, 15], 9
            )
        )
