from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifted_strings = defaultdict(list)
        for string in strings:
            shifted_string = self.get_shifted_strings(string)
            shifted_strings[shifted_string].append(string)
        return list(shifted_strings.values())

    def get_shifted_strings(self, s):
        first_char = s[0]
        shifted_string = ""
        for char in s:
            shifted_char = chr((ord(char) - ord(first_char) + 26) % 26 + ord("a"))
            shifted_string += shifted_char
        return shifted_string
