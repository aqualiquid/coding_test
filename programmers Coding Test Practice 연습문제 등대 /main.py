from typing import List, Tuple
from collections import defaultdict
import sys

sys.setrecursionlimit(200000)

def solution(n, lighthouse) -> int:
    def dfs(node: int, parent: int) -> Tuple[int, int]:
        not_light = 0
        light = 1

        for child in tree[node]:
            if child == parent:
                continue
            child_light, child_not_light = dfs(child, node)
            not_light += child_light
            light += min(child_light, child_not_light)

        return light, not_light

    tree = defaultdict(list)
    for a, b in lighthouse:
        tree[a].append(b)
        tree[b].append(a)

    root = 1
    light, not_light = dfs(root, -1)

    return min(light, not_light)
