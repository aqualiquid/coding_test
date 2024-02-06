# https://school.programmers.co.kr/learn/courses/30/lessons/12949
class Solution:
    def solution(arr1, arr2):
        answer = [[]]

        # counting row and col of 'arr1'and 'arr2' to multiply them.
        row1, col1 = len(arr1), len(arr1[0])
        row2, col2 = len(arr2), len(arr2[0])

        # generate empty matrix for submmiting result
        answer = [[0] * col2 for _ in range(row1)]

        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    answer[i][j] += arr1[i][k] * arr2[k][j]

        return answer