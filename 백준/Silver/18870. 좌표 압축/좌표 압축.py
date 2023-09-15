N = int(input())
numbers = list(map(int,input().split()))
num_list = list(sorted(set(numbers)))
dic = {num_list[i]:i for i in range (len(num_list))}
for i in numbers :
    print(dic[i],end=' ')