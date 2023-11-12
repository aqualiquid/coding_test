from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        lowest = prices[0]
        res = 0

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price-lowest)
        return res

    # Kadena's algorithm