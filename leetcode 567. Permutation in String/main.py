from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len: return False

        cnt_s1 = Counter(s1)
        window_cnt = Counter(s2[:s1_len])
        if window_cnt==cnt_s1: return True

        # now tbe window needs to be slided
        for i in range(s1_len, s2_len):
            window_cnt[s2[i-s1_len]] -= 1
            window_cnt[s2[i]] += 1

            #remove first index
            if window_cnt[s2[i-s1_len]]==0:
                del window_cnt[s2[i - s1_len]]
            if window_cnt==cnt_s1: return True

        return False


        return True




