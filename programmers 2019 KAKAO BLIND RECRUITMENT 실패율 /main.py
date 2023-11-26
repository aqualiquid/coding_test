# Problem description
# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    result = {}
    denominator = len(stages)

    for stage in range(1, N + 1):
        if denominator != 0:  # if denominator is NOT 0
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    sorted_stages = sorted(result, key=result.get, reverse=True)

    return sorted_stages
