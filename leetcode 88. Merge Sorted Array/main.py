from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return
        # Setup Pointers: Use three pointers:
        # i for indexing nums1 from the last initialized element (i.e., m-1).
        # j for indexing nums2 from the last element (i.e., n-1).
        # k for placing elements in the correct position
            # in nums1, starting from the end (i.e., m+n-1).
        i, j, k = m-1, n-1, m+n-1
        # Merge nums1 and nums2 in reverse order
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            else : # nums1[i] < nums2[j]
                nums1[k] =nums2[j]
                j -=1
            k-=1

        #Fill nums1 with remaining elements from nums2 if any
        while j>=0:
            nums1[k] =nums2[j]
            i-=1
            j-=1
        """
The time complexity for this merge algorithm is O(m + n), where m is the length of the first array (nums1) and n is the length of the second array (nums2).
This is because:

In the worst case, the algorithm needs to traverse both arrays completely
Each element is processed exactly once
The operations inside the loops (comparisons and assignments) are constant time

The space complexity is O(1) since the algorithm performs the merge in-place without requiring any extra space proportional to the input size.
        """