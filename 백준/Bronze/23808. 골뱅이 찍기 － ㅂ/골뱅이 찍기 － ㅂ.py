N = int(input())
first = ('@'*N) + ('   '*N) + ('@'*N)
second = ('@'*N*5)
for _ in range(N):
    print(first)
    print(first)
for _ in range(N):
    print(second)
for _ in range(N):
    print(first)
for _ in range(N):
    print(second)