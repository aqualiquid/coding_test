from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_maxSlidingWindow(self):
        solution = Solution()
        self.assertEqual(
            "BANC",
            solution.minWindow(
                "ADOBECODEBANC", "ABC"
            )
        )

    def test2_maxSlidingWindow(self):
        solution = Solution()
        self.assertEqual(
            "a",
            solution.minWindow(
                "a", "a"
            )
        )

    def test3_maxSlidingWindow(self):
        solution = Solution()
        self.assertEqual(
            '',
            solution.minWindow(
                "a", "aa"
            )
        )