from collections import defaultdict
# 백준 20922번 - 겹치는 건 싫어
# 홍대병에 걸려 겹치는 걸 매우 싫어하는 도현이
# 도현이를 위해 같은 원소가 K개 이하로 들어가는 최장 연속 부분 수열의 길이 구하기

# N : 수열 길이 / K : 같은 원소 K개 이하
N, K = map(int,input().split())
numbers = list(map(int,input().split()))

max_result = 0
left, right = 0, 0
count_dic = defaultdict(int)

while right < N :
  if count_dic[numbers[right]] < K :
    count_dic[numbers[right]] += 1
    right += 1
  else :
    count_dic[numbers[left]] -= 1
    left += 1
  max_result = max(max_result, right-left)

print(max_result)