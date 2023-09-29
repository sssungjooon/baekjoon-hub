text = str(input())
list = []
N = len(text)
for i in range(1,N+1):
    for j in range(0,N-i+1):
        list.append(text[j:j+i])
# print(list)
print(len(set(list)))