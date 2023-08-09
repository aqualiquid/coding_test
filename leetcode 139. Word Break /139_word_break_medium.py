from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if len(word)<=i:
                    if dp[i-len(word)]==True and s[i-len(word):i] ==word:
                        dp[i]= True
        return dp[n]

    def main(self):
        #s = "leetcode"
        #wordDict = ["leet", "code"]
        s ="a"
        wordDict =["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]
        print(self.wordBreak(s, wordDict))

if __name__ =="__main__":
    Solution().main()
