from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array to simplify logic
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        
        # Binary search for partitionX in nums1
        left, right = 0, x 

        while left <= right: # Changed to left <= right
            partitionX = (left + right) // 2
            # partitionY is calculated such that (partitionX + partitionY) is always equal to (x + y + 1) // 2
            # This ensures that we have (x + y + 1) // 2 elements on the left side of the combined sorted array
            partitionY = (x + y + 1) // 2 - partitionX

            # Define the four points to check
            # If partition is at 0, maxLeft is negative infinity
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # If partition is at x, minRight is positive infinity
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # check if we have found the correct partition (three cases for partition
            # 1. maxLeftX <= minRightY and maxLeftY <= minRightX
            # 2. maxLeftX > minRightY
            # 3. maxLeftY > minRightX
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We found the correct partitions
                # Calculate the median
                if (x + y) % 2 == 0:
                    # Even number of elements, median is the average of the two middle elements
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    # Odd number of elements, median is the single middle element
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # partitionX is too large, move to the left in nums1
                right = partitionX - 1
            else:
                # maxLeftY > minRightX, partitionX is too small, move to the right in nums1
                left = partitionX + 1
        
        # This part should ideally not be reached if the input arrays are valid.
        return 0.0 # Return 0.0 or raise an error as a fallback


