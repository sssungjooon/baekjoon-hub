def hansu(N) :
    hansu_count = 0
    for i in range(1, N+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_count += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_count += 1
    return hansu_count

N = int(input())
print(hansu(N))