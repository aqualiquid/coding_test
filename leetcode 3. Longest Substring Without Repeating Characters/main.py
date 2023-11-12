class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #sliding window
        seen = {}
        start = 0
        longest = 0

        for i,c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c]+1
            else:
                longest = max(longest, i - start + 1)
            seen[c] =i
        return longest
"""
pwwkew case:
(pw) w in seen and 
"""