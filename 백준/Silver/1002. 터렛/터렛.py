T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    rsum = r1 + r2
    rm = abs(r1 - r2)
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis == rsum or dis == rm:
            print(1)
        elif dis < rsum and dis > rm:
            print(2)
        else:
            print(0)