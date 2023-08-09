from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half_sum = int(sum(nums)/2)
        dp = [False] * (half_sum+1)
        dp[0] =True

        for num in nums:
            for i in range(half_sum, -1, -1):
                if dp[i] and i + num <= half_sum:
                    dp[num+i] = True
        return dp[half_sum]

    def main(self):
        #nums = [1, 5, 11, 5]
        nums =[1, 2]
        #nums = [1, 2, 3, 5]
        print(self.canPartition(nums))

if __name__ == "__main__":
    Solution().main()
