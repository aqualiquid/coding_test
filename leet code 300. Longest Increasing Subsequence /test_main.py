from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_longest_increasing_subsequence(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.lengthOfLIS(
                [10, 9, 2, 5, 3, 7, 101, 18]
            )
        )
    def test2_longest_increasing_subsequence(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.lengthOfLIS(
                [0,1,0,3,2,3]
            )
        )

    def test3_longest_increasing_subsequence(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.lengthOfLIS(
                [7,7,7,7,7,7,7]
            )
        )
