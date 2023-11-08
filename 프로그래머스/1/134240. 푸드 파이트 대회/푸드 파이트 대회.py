def solution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1) :
        # K는 앞뒤로 붙일 개수
        K = food[i]//2
        answer = str(i)*K + answer + str(i)*K
    return answer