from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_isAnagram(self):
        solution = Solution()
        self.assertEqual(
            True,
            solution.isAnagram(
                "anagram", "nagaram"
            )
        )

    def test2_isAnagram(self):
        solution = Solution()
        self.assertEqual(
            False,
            solution.isAnagram(
                "rat", "car"
            )
        )