class Solution:
    def numDecodings(self, s: str) -> int:
        s.upper()
        # Dynamic Programming
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # number of interpreting empty string is ONE
        dp[1] = 1  # number of interpreting only charter is ONE

        for i in range(2, n + 1):
            # dp[i-1], which is one number only, could be interpreted as valid number between 0 to 9
            # dp[i-2], which is two numbers, could be interpreted as valid number between 10 to 26 (i.e., EO Alphabet 'Z')
            one_number = int(s[i - 1:i])
            two_number = int(s[i - 2:i])

            if 1 <= one_number <= 9:
                # valid number
                dp[i] += dp[i - 1]
            if 10 <= two_number <= 26:
                # valid number
                dp[i] += dp[i - 2]
        return dp[n]