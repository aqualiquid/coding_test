from typing import List


class Solutions:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups= []
        for i in range(0, len(s), k):
            group = s[i:i+k]
            if len(group) < k:
                group += fill * (k - len(group))
            groups.append(group)
        return groups

    def main(self):
        s = "abcdefghi"
        k = 3
        fill = "x"
        print(self.divideString(s,k,fill))

if __name__ == "__main__":
    Solutions().main()