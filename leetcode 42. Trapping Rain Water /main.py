# referece: https://www.youtube.com/watch?v=ZI2z5pq0TqA
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # left, right pointer
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        water =0

        while left < right:
            if left_max < right_max:
                left_max = max(left_max, height[left])
                water+= left_max - height[left]
                left +=1
            else:
                right_max = max(right_max, height[right])
                water+= right_max - height[right]
                right -=1
        return water
    
    