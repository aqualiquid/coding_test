from unittest import TestCase
from main import Solution

class TestSolution(TestCase):
    def test1_trap(self):
        solution = Solution()
        self.assertEqual(
            6,
            solution.trap(
                [0,1,0,2,1,0,1,3,2,1,2,1]
            )
        )

    def test2_trap(self):
        solution = Solution()
        self.assertEqual(
            9,
            solution.trap(
                [4,2,0,3,2,5]
            )
        )
