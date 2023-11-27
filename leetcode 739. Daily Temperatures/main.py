from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # pair =[temp, idx]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                output[stack_idx] = abs(i - stack_idx)
            stack.append((t, i))
        return output
