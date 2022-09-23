N = int(input())
A = N//10
B = N%10
number = [A, B, A+B]
new_number = 0
cycle = 1

while number :
    new_number = number[1]*10 + (number[2])%10
    if new_number == N :
        break
    else :
        number = [new_number//10, new_number%10, (new_number//10)+(new_number%10)]
        cycle += 1
        continue
print(cycle)