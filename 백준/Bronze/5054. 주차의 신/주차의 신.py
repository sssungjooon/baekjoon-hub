import sys

t = int(input()) # 테스트 케이스 개수

for _ in range(t) : # 테스트 케이스 개수만큼 반복
    n = int(input()) # 방문할 상점 수 n
    shop = sorted(map(int, sys.stdin.readline().split())) # 상점 위치

    print((shop[-1] - shop[0])*2)