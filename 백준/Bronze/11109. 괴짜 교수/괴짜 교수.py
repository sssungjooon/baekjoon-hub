T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())

    # 병렬이 좋음
    if d + n*p < n*s:
        print("parallelize")
    elif d + n*p > n*s:
        print("do not parallelize")
    else:
        print("does not matter")