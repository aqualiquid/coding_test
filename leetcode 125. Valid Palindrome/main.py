from typing import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_string = re.sub(r'[^a-z0-9]', '', s.lower())

        # Compare characters from start and end
        n = len(modified_string)
        for i in range(n // 2):
            if modified_string[i] != modified_string[n - 1 - i]:
                return False
        return True
