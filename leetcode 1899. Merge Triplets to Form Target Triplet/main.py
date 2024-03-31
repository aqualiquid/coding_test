from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a, max_b, max_c = 0, 0, 0

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                max_a = max(max_a, triplet[0])
                max_b = max(max_b, triplet[1])
                max_c = max(max_c, triplet[2])

        return max_a == target[0] and max_b == target[1] and max_c == target[2]
