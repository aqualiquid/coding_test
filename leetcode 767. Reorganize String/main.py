from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count_char = Counter(s)
        max_count = max(count_char.values())
        if max_count > (n+1)//2:
            return ''

        idx = 0
        reorder = [None] * n
        for char, freq in count_char.most_common():
            while freq:
                reorder[idx] = char
                idx += 2
                freq -= 1
                if idx > n:
                    idx = 1
        return ''.join(reorder)