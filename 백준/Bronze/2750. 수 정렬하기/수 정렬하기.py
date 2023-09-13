N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

result = sorted(numbers)
for i in result :
    print(i)