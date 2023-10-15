from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_unique_paths(self):
        solution = Solution()
        self.assertEqual(
            [1,2],
            solution.twoSum(
                [2, 7, 11, 15],
                9
            )
        )

