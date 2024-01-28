def solution(n, tops):
    MOD = 10007
    dp = [[0, 0] for _ in range(n)]

    dp[0][0] = 3 if tops[0] == 1 else 2
    dp[0][1] = 1

    for i in range(1, n):
        if tops[i] == 1:
            dp[i][0] = (dp[i - 1][0] * 3 + dp[i - 1][1] * 2) % MOD
        else:
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD

    return (dp[n - 1][0] + dp[n - 1][1]) % MOD
