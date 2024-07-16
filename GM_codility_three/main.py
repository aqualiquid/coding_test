class Solution:
    def solution(self, S:str):
        l = len(S)
        dt = S+S
        answer = 0

        for idx in range(l):
            if dt[idx] == dt[idx+l-1]:
                answer += 1

        return answer