from typing import List
class Solution:
    # description of the DP- talbe
    # rows, i-direction, indicates all possible number of the amount
    # cols, j-direction, indicates all possible coins
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins)+1)]

        # DP-table initialization
        for i in range(len(coins)+1):
            dp[i][0] = 1

        # iteration for considering both cases: using the coin or not using the coin
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                # if the current value of 'j' is smaller than all possible coins, hence, you cannot make the amount by using the coin with all possible coins.
                if j< coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+ dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]
