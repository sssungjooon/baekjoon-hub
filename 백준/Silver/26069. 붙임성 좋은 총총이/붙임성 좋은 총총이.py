N = int(input())
rainbow = []
for _ in range(N):
    A, B = map(str,input().split())
    if A == 'ChongChong' :
       rainbow.append(B) 
    elif B == 'ChongChong' :
        rainbow.append(A)
    if A in rainbow :
        rainbow.append(B) 
    elif B in rainbow :
        rainbow.append(A)
result = len(set(rainbow))
print(result)