import heapq

def solution(jobs):
    jobs.sort()
    jobs_length = len(jobs)
    current_time, count, total_time = 0, 0, 0
    heap = []

    while count < jobs_length:
        while jobs and jobs[0][0] <= current_time:
            heapq.heappush(heap, (jobs[0][1], jobs[0][0]))
            jobs.pop(0)

        if heap:
            current_job = heapq.heappop(heap)
            start_time = max(current_time, current_job[1])
            current_time = start_time + current_job[0]
            total_time += current_time - current_job[1]
            count += 1
        else:
            if jobs:
                current_time = jobs[0][0]
            else:
                break
    return total_time // jobs_length