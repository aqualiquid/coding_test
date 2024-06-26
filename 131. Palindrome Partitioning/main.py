import copy
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # modified_string = re.sub(r'[^a-z0-9]','',s.lower())

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            # if the start approaches the end of len(s) indeed,
            if start == len(s):
                # it doesn't necesary to suse .deepcopy() since it already generated by new string
                # result.append(copy.deepcopy(path))
                result.append(path.copy())

                return

            for end in range(start, len(s)):
                # check if the current string is palindrome
                if isPalindrome(s[start:end + 1]):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    # remove the top element of the 'path
                    path.pop()

        result = []
        backtrack(0, [])
        return result
