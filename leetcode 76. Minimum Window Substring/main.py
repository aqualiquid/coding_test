import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ''
        targets = collections.Counter(t)
        tracks = collections.Counter()

        target_keys = set(targets.keys())

        # Find the left pointer's start position
        lt = next((idx for idx in range(len(s)) if s[idx] in target_keys), 0)

        for rt in range(lt, len(s)):
            if s[rt] in target_keys:
                tracks[s[rt]] += 1

                # Check if all characters are found and update left pointer
                while all(tracks[char] >= targets[char] for char in target_keys):
                    substring = s[lt: rt + 1]
                    if answer == '' or len(substring) < len(answer):
                        answer = substring

                    tracks[s[lt]] -= 1
                    lt = next((j for j in range(lt + 1, rt + 1) if s[j] in target_keys), lt)

        return answer
