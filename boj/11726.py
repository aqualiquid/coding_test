class Solutions:
    # 1×2, 2×1 타일로 채우는 방법
    # 2 x 1 라면 (1*2),(2*1)
    # 2 x 2 라면 (1*2)+(1*2), (2*1)+(2*1)
    # 2 x 3 라면 (1*2)+(1*2)+(1*2), (2*1)+(2*1)+(2*1), (1*2)+(2*1)+(2*1), (2*1)+(1*2)+(1*2)
    # 2 X n 라면 dp[i-1]+dp[i-2]
    def two_times_tiling(self, N:int) ->int:
        dp= [0] * 10007
        dp[0] =0
        dp[1] =1
        dp[2] =2
        for i in range(3, N+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[N]


    def main(self):
        num = int(input())
        print(self.two_times_tiling(num))

if __name__ == "__main__":
    Solutions().main()