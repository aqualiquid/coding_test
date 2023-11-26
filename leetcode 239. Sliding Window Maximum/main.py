# most of the code has been referred by CodePul's test method:' \
# Referece: https://github.com/skysign/WSAPT/blob/master/leetcode.com%20239.%20Sliding%20Window%20Maximum/main.py

from typing import List
from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heaps, ans =[], []
        idx =0
        window_lt, window_rt = idx, min(idx+k-1, len(nums)-1)

        for idx in range(window_lt, window_rt+1):
            heappush(heaps, (-nums[idx], idx))

        while (window_lt <= heaps[0][1] <= window_rt):
            heappop(heaps)

        ans.append(-heaps[0][0])

        return ans

