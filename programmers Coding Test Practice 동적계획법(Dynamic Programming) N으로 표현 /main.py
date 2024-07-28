class Solution:
    def solution(N, number):
        # 테스트 케이스 에러 부분
        if N == number:
            return 1

        # initializing into [ SET x 8 ] (N: 1 to 9)
        dp = [set() for x in range(8)]

        # initializing each set of "N" * i
        for i, x in enumerate(dp, start=1):
            x.add(int(str(N) * i))

        # 3. n 일반화
        #   {
        #       "n" * i U
        #       1번 set 사칙연산 n-1번 set U
        #       2번 set 사칙연산 n-2번 set U
        #       ...
        #       n-1번 set 사칙연산 1번 set,
        #    }
        # number를 가장 최소로 만드는 수 구함
        for i in range(1, 8):
            for j in range(i):
                for op1 in dp[j]:
                    for op2 in dp[i - j - 1]:
                        dp[i].add(op1 + op2)
                        dp[i].add(op1 - op2)
                        dp[i].add(op1 * op2)
                        if op2 != 0:
                            dp[i].add(op1 // op2)

            if number in dp[i]:
                answer = i + 1
                break

        else:
            answer = -1

        return answer