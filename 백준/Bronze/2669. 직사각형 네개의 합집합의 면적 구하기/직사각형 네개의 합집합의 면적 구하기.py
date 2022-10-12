# 사각형들 담을 리스트
square_lst = []

# 최댓값 담을 리스트
max_lst = []

# 입력은 네줄이라고 명시되어있다.
for test_count in range(4) :
    x1, y1, x2, y2 = map(int,input().split())
    square = [x1, y1, x2, y2]
    max_lst.append(max(square))
    square_lst.append(square)

# 최대 범위를 N으로 설정한다
N = max(max_lst)

# N을 기준으로 큰 체크리스트를 만든다
check = []
for _ in range(N):
    check.append([0]*N)

# check에 직사각형이 있는 부분은 더해준다
for sq in square_lst :
    for i in range(sq[0], sq[2]) :
        for j in range(sq[1], sq[3]) :
            check[i][j] += 1

# 이 과정이 끝났으면 check 원소가 0이 아닌 곳을 count
count = 0
for i in range(N):
    for j in range(N):
        if check[i][j] > 0 :
            count += 1

print(count)