N = int(input())
numbers = list(map(int,input().split()))
v = int(input())
check = 0
for num in numbers :
    if num == v :
        check += 1

print(check)