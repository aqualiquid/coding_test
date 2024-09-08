import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
min_heap = []
result = []

for i in range(1, N + 1):
    x = int(data[i])

    if x > 0:
        heapq.heappush(min_heap, x)
    else:
        if min_heap:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)
