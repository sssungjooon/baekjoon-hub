# 첫줄 테스트 케이스 T
T = int(input())
for test_count in range(T):

    k = int(input())
    n = int(input())

    apt = [(i+1) for i in range(n)]
    new_floor = []

    for _ in range(k):
        temp = 0
        for a in apt :
            temp += a
            new_floor.append(temp)
        apt = new_floor
        new_floor = []
    print(apt[-1])
