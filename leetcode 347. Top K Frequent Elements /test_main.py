from unittest import TestCase
from main import Solution

class TestSolutions(TestCase):
    def test1_group_anagram(self):
        solution = Solution()
        self.assertEqual(
            [["bat"],["nat","tan"],["ate","eat","tea"]],
            solution.groupAnagrams(
                ["eat","tea","tan","ate","nat","bat"]
            )
        )