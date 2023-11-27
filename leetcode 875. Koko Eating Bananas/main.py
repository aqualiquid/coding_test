import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res=-1

        while l<=r :
            mid = (l+r)//2
            t_times=0
            for p in piles:
                t_times += math.ceil(p / mid)
            if t_times <= h:
                res= mid
                r = mid-1
            else:
                l= mid+1
        return res

