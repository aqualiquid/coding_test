def is_safe(row, col, n, queens):
    """
    현재 위치에 퀸을 안전하게 배치할 수 있는지 확인합니다.
    - 수직, 대각선 방향에 다른 퀸이 없어야 합니다.
    """

    for i in range(row):
        # 같은 열에 퀸이 있는지 확인
        if queens[i] == col:
            return False

        # 대각선에 퀸이 있는지 확인 (열의 차이와 행의 차이가 같으면 대각선상에 위치)
        if abs(queens[i] - col) == abs(i - row):
            return False

    return True


def solve_queens(row, n, queens, solutions):
    """
    퀸을 체스판에 배치하는 함수입니다. 백트래킹을 사용하여 모든 가능한 경우를 탐색합니다.
    """
    if row == n:
        # 모든 행에 퀸을 배치했으면, 해결책을 저장합니다.
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_safe(row, col, n, queens):
            # 현재 위치가 안전하면 퀸을 배치하고, 다음 행으로 이동합니다.
            queens[row] = col
            solve_queens(row + 1, n, queens, solutions)
            # 현재 위치에 퀸을 배치하는 것이 최종 해결책으로 이어지지 않으면, 백트래킹을 통해 다른 열을 시도합니다.


def solve_n_queens(n):
    """
    N-Queens 문제의 모든 해결책을 찾습니다.
    """
    solutions = []  # 모든 해결책을 저장할 리스트
    queens = [-1] * n  # 각 행의 퀸이 위치한 열을 저장합니다. 초기값은 -1로, 아직 퀸이 배치되지 않음을 의미합니다.
    solve_queens(0, n, queens, solutions)  # 0번 행부터 시작하여 퀸을 배치합니다.

    # 해결책의 개수를 반환합니다. 해결책 자체를 보고 싶다면 solutions 리스트를 출력하거나 반환할 수 있습니다.
    return len(solutions)


# 예제 실행
N = 4
print(f"4x4 체스판에 퀸을 배치하는 경우의 수: {solve_n_queens(N)}")

# https://chat.openai.com/c/f6cc5762-c6ac-4815-a016-b95cbce2b02e
# N-queen explain : https://oeis.org/A002562