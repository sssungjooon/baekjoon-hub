numbers = input()
arr = []
for n in numbers :
    arr.append(int(n))
arr2 = sorted(arr,reverse=True)
result = ''
for a in arr2 :
    result += str(a)
print(int(result))