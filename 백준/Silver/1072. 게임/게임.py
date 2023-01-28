import sys

# 특정값을 만족하는지 확인하는 구간
def sol(x,y,z,m) :
    next_y = (y + m) * 100
    next_x = (x + m)
    next_z = next_y // next_x

    if next_z == z :
        return False
    else :
        return True


#변수 입력 구간
x,y = map(int,sys.stdin.readline().split())
z = (y * 100) // x

#예외 설정
if x==y :
    print(-1)
elif z == 99 :
    print(-1)

#이진 탐색 구간
else :
    answer = 0
    l,r = 0, sys.maxsize
    while l < r :
        m = (l + r  ) // 2
        if sol(x, y, z, m ) :
            r = m
            answer = m
        else :
            l = m + 1
    print(answer)