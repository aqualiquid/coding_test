"""
Pusedo Code:
(1) 카드 N개를 구하기 위한 dp 솔루션 테이블을 초기화
(2) iterative statement 을 통해
"""
class Solutions:
    def purchasing_card(self, N:int, P:list) ->int:
        # initializing 'dp' solution table
        dp = [0] * (N+1)
        #dp[0]= 0

        for i in range(1, N+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]+P[j-1])
        return dp[N]

    def main(self):
        num = int(input())
        period= list(map(int, input().split()))
        print(self.purchasing_card(num, period))

if __name__ == "__main__":
    Solutions().main()