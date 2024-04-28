from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_dic = {"2": "abc", "3": "def", "4": "ghi", \
        "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = ['']

        for digit in digits:
            tmp=[]
            for strings in digit_dic[digit]:
                for char in output:
                    tmp.append(char+strings)
            output = tmp

        return output
