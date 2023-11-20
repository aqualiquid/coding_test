from unittest import TestCase
from main_defaultdict import Solution_dict

class TestSolution(TestCase):
    def test1_checkInclusion(self):
        solution = Solution_dict()
        self.assertEqual(
            True,
            solution.checkInclusion(
                "ab", "eidbaooo"
            )
        )

    def test2_checkInclusion(self):
        solution = Solution_dict()
        self.assertEqual(
            False,
            solution.checkInclusion(
                "ab", "eidboaoo"
            )
        )
