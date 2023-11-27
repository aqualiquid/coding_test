from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_LCS(self):
        solution = Solution()
        self.assertEqual(
            3,
            solution.longestCommonSubsequence(
                "abc",
                "abc"
            )
        )

    def test2_LCS(self):
        solution = Solution()
        self.assertEqual(
            3,
            solution.longestCommonSubsequence(
                "abcde",
                "ace"
            )
        )

    def test3_LCS(self):
        solution = Solution()
        self.assertEqual(
            0,
            solution.longestCommonSubsequence(
                "abc",
                "def"
            )
        )