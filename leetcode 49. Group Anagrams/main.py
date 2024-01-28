import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            s

        return anagrams.values()
        #["eat","tea","tan","ate","nat","bat"]
