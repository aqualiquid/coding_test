class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

            return output

        if len(s) < 2 or s[::-1] == s[:]:
            return s
        # even, odd
        result = ''
        for i in range(len(s) - 1):
            result = max(result, extend(i, i + 1), extend(i, i + 2), key=len)
        return result


