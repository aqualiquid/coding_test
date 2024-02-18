import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add new value to the heap
        heapq.heappush(self.heap, val)
        # If heap size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The smallest element in the heap is the kth largest element
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)