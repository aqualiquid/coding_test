from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_findMin(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.findMin(
                [3,4,5,1,2]
            )
        )

    def test2_findMin(self):
        solution = Solution()
        self.assertEqual(
            0,
            solution.findMin(
                [4,5,6,7,0,1,2]
            )
        )

    def test3_findMin(self):
        solution = Solution()
        self.assertEqual(
            11,
            solution.findMin(
                [11,13,15,17]
            )
        )
