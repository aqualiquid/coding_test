import sys
from typing import List
# https://www.acmicpc.net/problem/2805
''' (sample input)
4 7
20 15 10 17
'''

def get_wood_length(trees, height):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree-height
    return total

def solve():
    answer = 0
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    right = max(trees)
    left = 0

    while left <= right:
        mid = (left + right) // 2
        # return the sliced tree piece
        wood = get_wood_length(trees, mid)
        # case: if the collected woods is equal or greater than the target amount of woods, increase the hegight of the saw, which gives you less total amounts
        if wood >= M:
            answer = mid
            left = mid+1
        # case: if the collected woods is smaller than the target amount of woods, decrease the height of the saw, whch gives you more total amounts,
        else:
            right = mid-1
    return answer



if __name__ == '__main__':
    print(solve())

