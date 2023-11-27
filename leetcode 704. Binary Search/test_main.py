from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_search(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.search(
                [-1,0,3,5,9,12],
                9
            )
        )
