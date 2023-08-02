from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numbers, letters =[], []
        for log in logs:
            if log.split()[1].isdigit():
                numbers.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return numbers+letters

    def main(self):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        print(self.reorderLogFiles(logs))

if __name__ == "__main__":
    Solution().main()
