n, w, L = map(int,input().split())

truck = list(map(int,input().split()))
bridge = [0]*w

time_count = 0

while bridge :
    time_count += 1 
    bridge.pop(0)
    # 트럭이 남아있다면
    if truck:
        # 다리 최대 하중보다 현재 입장할 트럭 합친 하중이 더 크다면 빈 공간이 입장
        if sum(bridge) + truck[0] > L:
            bridge.append(0)
        # 다리 최대 하중보다 현재 입장할 트럭 합친 하중이 적으면 입장
        else:
            bridge.append(truck.pop(0))
print(time_count)