def solution(n, control):
    answer = n
    for S in control :
        if S == "w" :
            answer += 1
        elif S == "s" :
            answer -= 1
        elif S == "d" :
            answer += 10
        elif S == "a" :
            answer -= 10
    return answer