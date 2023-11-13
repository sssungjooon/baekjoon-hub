N = int(input())
first = '@'*N
second = '@'*5*N
for _ in range(N*4):
    print(first)
for _ in range(N):
    print(second)