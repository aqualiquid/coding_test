from typing import List

class Union_Find:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False

        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else: # self.rank[rootP] == self.rank[rootQ]
            #그러나 이제 rootP의 트리 높이가 실제로 1 증가할 수 있습니다.
            #왜냐하면 같은 높이의 트리가 rootP에 추가되므로 rootP 아래에 새로운 "수준"이 생기게 됩니다.
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = Union_Find(n +1) # func 'union_find' stats from 1 to n (1-idxed)

        redundant_edge = None
        for a, b in edges:
            if not uf.union(a, b):
                redundant_edge =[a, b]

        return redundant_edge
