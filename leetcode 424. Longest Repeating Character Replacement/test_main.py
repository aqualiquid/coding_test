from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_characterReplacement(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.characterReplacement(
                "ABAB", 2
            )
        )
    def test2_characterReplacement(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.characterReplacement(
                "AABABBA", 1
            )
        )
