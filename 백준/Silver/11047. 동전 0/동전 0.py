# 준규가 가지고 있는 동전 N 종류
# 그 가치의 합을 K로 만들기
# 이 때 필요한 동전 개수 최소값 구하는 프로그램
N, K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

# print(coins)
# 코인 개수를 셀 변수
count = 0

# 동전들이 오름차순으로 주어지므로 뒤에서부터 크다.
for i in range(N-1,-1,-1) :
    change = 0
    if K >= coins[i] :
        count += K // coins[i]
        change = K % coins[i]
        K = change
    elif K < coins[i] :
        continue
    if K == 0 :
        break
print(count)
