import collections
from typing import List


class Solutions:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        return anagrams.values()

    def main(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(self.groupAnagrams(strs))

if __name__ == "__main__" :
    Solutions().main()


