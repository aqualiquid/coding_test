from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int: #sliding window
        counter_dict = defaultdict(int)
        mx = 0

        lt = 0
        for rt in range(len(s)):
            counter_dict[s[rt]] += 1

            window_length = rt-lt +1
            max_count = max(counter_dict.values())

            if (window_length -max_count ) > k:
                counter_dict[s[lt]] = -1
                lt += 1

            mx = max(mx, rt+1-lt)


        return mx
