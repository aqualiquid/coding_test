from typing import List

class Solution_diff:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # pair =[temp, idx]
        #for i, t in enumerate(temperatures):


