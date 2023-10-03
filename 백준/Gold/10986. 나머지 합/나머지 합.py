import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0]*(N+1) # 부분합 리스트 (단, M으로 나눈 나머지로 저장)

# count[idx]는 1부터 x까지의 부분합이 담긴
# (정확하는 M으로 나눈 나머지가 담긴)
# p_sum의 원소들 중에, 그 값이 idx인 것의 개수를 의미함
count = [0]*(M+1)

# p_sum과 count 구하기
for i in range(N):
    p_sum[i+1] = (p_sum[i] + arr[i]) % M
    count[p_sum[i+1]] += 1

# 1부터 x까지의 부분합을 M으로 나눈 나머지가 0이라면,
# 그 부분합 자체로 하나를 카운팅해줘야됨
ans = count[0]

# 그 외의 부분합들을 처리하는 구문임.
# 만약 어떤 두 부분합(1부터 x까지의)을 M으로 나눈 나머지가 같고
# 각각 1부터 a, b 까지의 부분합이라고 가정하면,
# a+1부터 b까지의 부분합은 M으로 나누어떨어진다.
# 이 부분은 수학적인 논리이므로 잘 생각해보자.
for i in range(M+1):
    # 뽑는 개수가 2인 combination의 변형식임
    ans += (count[i] * (count[i]-1)) // 2
    
print(ans)