N, K = map(int,input().split())
ali = []
for i in range(1,N+1):
    if N%i == 0 :
        ali.append(i)
if len(ali) < K : 
    print(0)
else : 
    print(ali[K-1])