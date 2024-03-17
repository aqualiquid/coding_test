
from unittest import TestCase
from main import Solutions

class TestFindMinIntercepts(TestCase):
    def test_example(self):
        solution = Solutions()
        self.assertEqual(
            3,
            solution.life_saving_boat(
                [70, 50, 80, 50], 100
            )
        )

    def test_example_2(self):
        solution = Solutions()
        self.assertEqual(
            3,
            solution.life_saving_boat(
                [70, 80, 50], 100
            )
        )