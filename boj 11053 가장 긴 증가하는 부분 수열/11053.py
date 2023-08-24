# https://www.acmicpc.net/problem/11053
# hint: exactly same with Leetcode LIS problem
class Solution:
    def LIS(self, seq_um:int, nums: str)-> int :
        nums = list(map(int, nums.split()))
        if not nums: return 0
        dp = [1] * seq_um
        for i in range(1,seq_um):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i], dp[j-1]+1)
        return max(dp)

    def main(self):
        sequence = 6
        list_num = "10 20 10 30 20 50"
        print(self.LIS(sequence,list_num))

if __name__== "__main__":
    Solution().main()

"""
예제 입력 1
6
10 20 10 30 20 50
예제 출력 1
4
"""