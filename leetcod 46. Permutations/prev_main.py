class Solution:
    def permute(self, nums):
        result = []
        self._permute(nums, 0, result)
        return result

    def _permute(self, nums, begin, result):
        if begin >= len(nums):
            result.append(nums[:])  # Make a deep copy of nums and add to result
            return
        for i in range(begin, len(nums)):
            self._swap(nums, begin, i)  # Swap the elements at indices begin and i
            self._permute(nums, begin + 1, result)  # Recurse with the next element
            self._swap(nums, begin, i)  # Swap back to backtrack

    def _swap(self, nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]  # Swap elements at indices x and y

# Example usage
sol = Solution()
print(sol.permute([1, 2, 3]))
