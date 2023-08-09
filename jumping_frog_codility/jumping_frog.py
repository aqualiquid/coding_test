# Time complexity K*O(n)
import collections
class Solutions:

    def min_jumping_trial(self, N:int, K:int)-> int:
        dp = [float('inf')] * (N+1)
        dp[0] =0
        for i in range(1,N+1):
            for j in range(1, min(i,K)+1):
                dp[i]= min(dp[i], dp[i-j]+1)
        return dp[N]

    def main(self):     # assume N is 10, and K is 3
        n= 10
        k= 3
        print(self.min_jumping_trial(n,k))

if __name__ =="__main__":
    Solutions().main()