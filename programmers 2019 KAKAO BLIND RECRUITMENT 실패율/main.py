# https://school.programmers.co.kr/learn/courses/30/lessons/42889
class Solution:
    def getFailureRates(self, N, stages):
        # 실패율을 저장할 딕셔너리
        failure_rates = {}

        # 현재 스테이지에 있는 플레이어 수
        players_remaining = len(stages)

        for stage in range(1, N + 1):
            if players_remaining != 0:
                # 현재 스테이지에 머물러 있는 플레이어 수 계산
                players_stuck = stages.count(stage)

                # 실패율 계산
                failure_rate = players_stuck / players_remaining

                # 실패율 딕셔너리에 추가
                failure_rates[stage] = failure_rate

                # 다음 스테이지의 플레이어 수 갱신
                players_remaining -= players_stuck
            else:
                # 남은 플레이어가 없으면 실패율은 0
                failure_rates[stage] = 0

        # 실패율을 기준으로 스테이지 번호를 내림차순으로 정렬
        sorted_stages = sorted(failure_rates, key=lambda x: failure_rates[x], reverse=True)

        return sorted_stages
