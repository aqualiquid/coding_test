from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_longestConsecutive(self):
        solution = Solution()
        self.assertEqual(
            4,
            solution.longestConsecutive(
                [100,4,200,1,3,2]
            )
        )
    def test2_longestConsecutive(self):
        solution = Solution()
        self.assertEqual(
            9,
            solution.longestConsecutive(
                [0,3,7,2,5,8,4,6,0,1]
            )
        )
