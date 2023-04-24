# 첫째줄에 N, M (N개의 바구니 M번 바꾸기)
N, M = map(int,input().split())
basket = [i for i in range(1,N+1)]
# M번 바꾸기
for i in range(M):
    i, j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
# 출력
for i in range(N):
    print(basket[i], end=' ')