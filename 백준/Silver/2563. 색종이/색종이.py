# 색종이의 수 N
N = int(input())
# 100 X 100 판 만들기
paper = []
for _ in range(100):
    temp = [0]*100
    paper.append(temp)

for test in range(N):
    x, y = map(int,input().split())
    for i in range(x,x+10) :
        for j in range(y,y+10):
            paper[i][j] += 1

result = 0
# 도화지에서 0이 아닌 곳의 크기를 모두 출력
for i in range(100):
    for j in range(100):
        if paper[i][j] != 0 :
            result += 1

print(result)