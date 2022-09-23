stack = []

T = int(input())
for _ in range(T):
    N = int(input())
    if N != 0 :
        stack.append(N)
    elif N == 0 :
        stack.pop()
print(sum(stack))