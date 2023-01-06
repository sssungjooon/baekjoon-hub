# 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램
# 숫자 배열 담을 2차원 배열
numbers = []
# 최대값
max_num = 0
x = 1
y = 1
for _ in range(9):
    num = list(map(int,input().split()))
    numbers.append(num)

for i in range(9):
    for j in range(9):
        if numbers[i][j] > max_num :
            max_num = numbers[i][j]
            x = i + 1
            y = j + 1

print(max_num)
print(f'{x} {y}')