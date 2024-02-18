class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a min heap
        min_heap = []

        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(min_heap, (dist, [x, y]))

        # Extract the k closest points from the min heap
        closest_points = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return closest_points