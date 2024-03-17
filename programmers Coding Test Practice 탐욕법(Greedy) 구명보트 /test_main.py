
from unittest import TestCase
from main import Solutions

class TestFindMinIntercepts(TestCase):
    def test_example(self):
        solution = Solutions()
        self.assertEqual(
            3,
            solution.find_min_intercept(
                [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
            )
        )

    def test_example_2(self):
        solution = Solutions()
        self.assertEqual(
            1,
            solution.find_min_intercept(
                [[1, 10], [2, 5], [3, 8]]
            )
        )