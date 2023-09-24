from unittest import TestCase
from main import TimeMap

class TestSolution(TestCase):
    def test1_findMin(self):
        solution = TimeMap()
        self.assertEqual(
            [None, None, "bar", "bar", None, "bar2", "bar2"],
            solution.findMin(
                ["TimeMap", "set", "get", "get", "set", "get", "get"]
                [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
            )
        )
