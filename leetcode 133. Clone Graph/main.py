"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
import collections


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # ininitialize dict by using defaultdic
        clone_dict = collections.defaultdict(lambda: Node())

        # DFS stack initlization
        dfs_stack = [node]

        clone_dict[node].val = node.val

        while dfs_stack:
            current = dfs_stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in clone_dict:
                    dfs_stack.append(neighbor)
                    clone_dict[neighbor].val = neighbor.val

                clone_dict[current].neighbors.append(clone_dict[neighbor])

        return clone_dict[node]

