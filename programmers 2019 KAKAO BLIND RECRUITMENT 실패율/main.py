# https://school.programmers.co.kr/learn/courses/30/lessons/42889
class Soltuion:
    def solution(N, stages):
        result = {}
        denominator= len(stages)#stage의 개수 정의
        for stage in range(1,N+1): #stage 범위 반복문
            if denominator!=0: #denominator가 0이 아닌경우
                count = stages.count(stage)#stage에 들어오는 숫자와 같은 숫자의 개수를 센다
                result[stage]=count/denominator
                denominator-=count
            else:
                result[stage]=0
        return sorted(result,key=lambda x: result[x],reverse=True)

