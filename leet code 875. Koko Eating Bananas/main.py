import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, max(piles)
        res=-1

        while l<=r :
            k = (l+r)//2
            t_times=0
            for p in piles:
                t_times += math.ceil(p / k)
            if t_times <= h:
                res= k
                r = k-1
            else:
                l= k+1
        return res