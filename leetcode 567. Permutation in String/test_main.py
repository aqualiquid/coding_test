from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_checkInclusion(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.checkInclusion(
                "ab", "eidbaooo"
            )
        )

    def test2_checkInclusion(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.checkInclusion(
                "ab", "eidboaoo"
            )
        )
