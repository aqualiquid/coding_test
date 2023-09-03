from unittest import TestCase
from main import Solution


class TestSolution(TestCase):
    def test1_Fibonacci_Numbe(self):
        solution = Solution()
        self.assertEqual(
            1,
            solution.fib(
            2
            )
        )

    def test2_Fibonacci_Numbe(self):
        solution = Solution()
        self.assertEqual(
            3,
            solution.fib(
            4
            )
        )

    def test3_Fibonacci_Numbe(self):
        solution = Solution()
        self.assertEqual(
            2,
            solution.fib(
            3
            )
        )

