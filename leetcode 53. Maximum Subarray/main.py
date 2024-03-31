class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        # for num in nums:
        #     current_sum = max(num, current_sum + num)
        #     max_sum = max(max_sum, current_sum)

        return max_sum

    # 기존 방법이 틀려서 (주석 부분) 다시 올림.. 정확히 뭐가 잘못된건지...