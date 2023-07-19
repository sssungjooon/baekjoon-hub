# 첫쨰줄에 계단의 개수
N = int(input())
step = []
for _ in range(N):
    number = int(input())
    step.append(number)
dp=[0]*(N) # dp 리스트
if len(step)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(step))
else: # 계단이 3개 이상일 때
    dp[0]=step[0] # 첫째 계단 수동 계산
    dp[1]=step[0]+step[1] # 둘째 계단까지 수동 계산
    for i in range(2,N): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])
    print(dp[-1])