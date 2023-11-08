# 포켓몬의 종류 수 N
N = int(input())
pocket = []
dogam = []
for i in range(N):
    P  = str(input())
    # 진화에 필요한 사탕 수 K, 지우가 갖고 있는 사탕 수 M
    K, M = map(int,input().split())
    # 진화 수
    evo = 0
    # pocket.append([P,K,M,0])
    while True :
        if K > M :
            break
        else :
            M = M-K+2
            evo += 1
    pocket.append([P,evo,i])
    dogam.append([i,P])
# print(pocket)

# 진화시킬 수 있는 포켓몬의 총 마리 수 
result = 0
for i in range(N):
    result += pocket[i][1]
print(result)
# 가장 많이 진화시킬 수 있는 포켓몬의 이름
last = sorted(pocket, key=lambda x:(-x[1], x[2]) )
# print(last)
print(last[0][0])