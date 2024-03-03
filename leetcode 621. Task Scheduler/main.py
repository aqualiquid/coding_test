import heapq
from collections import Counter


# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def push(self, val):
#         heapq.heappush(self.heap, -val)

#     def pop(self):
#         return -heapq.heappop(self.heap)

#     def __len__(self):
#         return len(self.heap)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_counter = Counter(tasks)
        max_heap = [-count for count in task_counter.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count < -1:
                        temp.append(count + 1)
                time += 1
                if not max_heap and not temp:
                    break

            for item in temp:
                heapq.heappush(max_heap, item)
        return time
