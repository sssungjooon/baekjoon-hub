num1 = int(input())
num2 = list(map(int,input()))

print(num1*num2[2])
print(num1*num2[1])
print(num1*num2[0])

result = (num1*num2[2]) + (num1*num2[1])*10 + (num1*num2[0])*100
print(result)
