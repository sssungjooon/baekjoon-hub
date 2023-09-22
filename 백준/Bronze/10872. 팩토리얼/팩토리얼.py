N = int(input())
result = 1
while True :
    if N == 0 :
        break
    else :
        result *= N
        N -= 1
print(result)