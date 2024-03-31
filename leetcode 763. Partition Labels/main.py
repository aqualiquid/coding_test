from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i

        start, end = 0, 0
        result = []
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(i - start + 1)
                start = i + 1

        return result