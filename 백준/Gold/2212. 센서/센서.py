import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if k >= n:
    print(0)
else:
    index = list(map(int, input().split()))
    index.sort()

    diff = []
    for i in range(len(index)-1):
        diff.append(index[i+1] - index[i])  # 각 구간의 거리를 담은 배열

    diff.sort()  # 오름차순 정렬하고 
    for i in range(k-1):
        diff.pop()  # 거리가 긴 구간부터 잘라주면 되는데 해당 구간을 없애버리면 그게 잘라진거다.

    print(sum(diff))