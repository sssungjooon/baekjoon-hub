import heapq

# 첫째 줄에 N이 주어진다.
N = int(input())
heap = []

for line in range(N) :
    numbers = list(map(int,input().split()))
    for number in numbers :
        # heap의 크기가 N보다 작다면 숫자 넣기
        # heap의 크기를 N으로 유지 (그래야 N번째 큰 수가 )
        if len(heap) < N :
            # heapq.heappush(heap, item)을 이용해 item을 heap에 추가
            heapq.heappush(heap, number)
        else :
            if heap[0] < number :
                # heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 
                # 비어 있는 경우 IndexError가 호출됨. 
                heapq.heappop(heap)
                heapq.heappush(heap, number)

print(heap[0])