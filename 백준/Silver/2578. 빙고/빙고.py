# 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수 (1부터 25까지의 자연수)
arr = []
for _ in range(5):
    temp = list(map(int,input().split()))
    arr.append(temp)

# 그 이후 사회자가 부르는 번호가 다섯줄 나온다.
# 이 번호는 2차원 배열이 아닌 리스트에 그냥 담는다.
call_number = []
for _ in range(5):
    call_temp = list(map(int,input().split()))
    for k in call_temp :
        call_number.append(k)

# 몇번째 수인지 카운트할 변수
count = 0

# 몇번째 빙고인지 카운트할 변수
bingo = 0

# 
while True :
    # 맨 앞부터 숫자 하나씩 뺀다.
    call = call_number.pop(0)
    # 매 숫자 부를 때마다 빙고 초기화
    bingo = 0
    # 빙고 판에서 해당 숫자 탐색
    # 그 숫자를 찾으면 0으로 바꿔서 빙고 표시
    for i in range(5):
        for j in range(5):
            if arr[i][j] == call :
                arr[i][j] = 0
                count += 1
    # 가로부터 확인
    for r in range(5):
        num_list = []
        for c in range(5):
            num_list.append(arr[r][c])
        if num_list == [0]*5 :
            bingo += 1

    # 세로
    for c in range(5):
        num_list = []
        for r in range(5):            
            num_list.append(arr[r][c])
        if num_list == [0]*5 :
            bingo += 1
    
    # 대각선 왼쪽에서 오른쪽으로
    num_list = []
    for r in range(5):
        num_list.append(arr[r][r])
    if num_list == [0]*5 :
        bingo += 1
    
    # 대각선 오른쪽에서 왼쪽
    num_list = []
    for r in range(5):
        num_list.append(arr[r][4-r])
    if num_list == [0]*5  :
        bingo += 1

    if bingo >= 3 :
        break

print(count) 