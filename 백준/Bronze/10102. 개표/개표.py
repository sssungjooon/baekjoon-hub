# 첫 줄에는 심사 위원의 수
N = int(input())

# 누구 투표 인풋
vote = list(input())

A_count = 0
B_count = 0

for i in range(N):
    if vote[i] == 'A' :
      A_count += 1
    elif vote[i] == 'B':
      B_count += 1

# 결과 출력
if A_count == B_count :
  print('Tie')
elif A_count > B_count :
  print('A')
elif A_count < B_count :
  print('B')