# referece: https://www.youtube.com/watch?v=ZI2z5pq0TqA
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # left height
        # right height

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                # left_max > right_max:
                # things that you should know that, we need to consider the followings:
                # right_max = left_max
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result

