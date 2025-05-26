class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left  = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    def binSearch(self, sub_nums, target, left_biased:bool):
        i =-1
        left, right = 0, len(sub_nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > sub_nums[mid]:
                left = mid + 1
            elif target < sub_nums[mid]:
                right = mid - 1
            else:
                i = mid
                if left_biased :
                    right = mid - 1
                else:
                    left = mid + 1
        return i