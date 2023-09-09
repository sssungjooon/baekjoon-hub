N = int(input())
numbers = []
number = 0
while True :
    if len(numbers) == N :
        break
    else :
        number += 1
        check = str(number)
        if check.count('666') >= 1 :
            numbers.append(number)
print(numbers[-1])