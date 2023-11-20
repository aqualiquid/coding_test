from collections import Counter, defaultdict


class Solution_dict:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        if s1 == s2: return True

        s1_dict = Counter(s1)
        s2_dict = defaultdict(int)

        for rt in range(len(s1), len(s2) + 1):
            s2_dict.clear()
            lt = rt - len(s1)

            for idx in range(lt, rt):
                s2_dict[s2[idx]] += 1

            if s1_dict == s2_dict:
                return True

        return False