from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_subsets(self):
        solution = Solution()
        self.assertEqual(
            {frozenset()},
            {frozenset(x) for x in solution.subsets([])}
        )

        self.assertEqual(
            {frozenset(), frozenset([1]), frozenset([2]), frozenset([1,2]), frozenset([3]), frozenset([1,3]), frozenset([2,3]), frozenset([1,2,3])},
            {frozenset(x) for x in solution.subsets([1, 2, 3])}
        )

    def test2_subsets(self):
        solution=Solution()
        self.assertEqual(
            {frozenset(), frozenset([0])},
            {frozenset(x) for x in solution.subsets([0])}
        )
