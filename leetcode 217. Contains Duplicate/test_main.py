from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_containsDuplicate(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.containsDuplicate(
                [1,2,3,1]
            )
        )

    def test2_containsDuplicate(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.containsDuplicate(
                [1,2,3,4]
            )
        )