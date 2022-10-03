
T = 10

for test_count in range (1, T+1) :
    width = int(input())
    heights = list(map(int, input().split()))

    view_house = 0
    # 맨 왼쪽 두칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다.
    # 그러므로 범위는 2부터 전체 너비의 -2까지
    for idx in range(2, width-2):
        # 선택된 집을 중심으로 양쪽 두칸, 선택된 집을 제외한 양쪽 총 4개의 집들을 높이를 near_house로 묶는다.
        near_house = [heights[idx-2], heights[idx-1], heights[idx+1], heights[idx+2]]
        # 이웃집 4집 중 최고 높이를 가진 집의 높이 max_height
        max_height = 0
        for near in near_house :
            # 조망이 2칸 이상 확보되려면 양쪽 2집들보다 높이가 무조건 높아야 확보될 수 있다.
            # 그러므로 조망 확보한 세대를 구하는 전제 조건이 양쪽 총 4개의 집들보다 높은 집이여야 하고,
            # 그 높은 집의 최대 높이에서 양쪽 총 4집 중 최고 높이를 뺀 값이 조망 확보 세대 수이다. 
            # 따라서 필요한 값은 1. 양쪽 2칸의 집들보다 높은 집의 높이 값과,
            # 2. 양쪽 총 4칸의 이웃집 중 최고 높이를 가진 집의 높이 값이 필요하다. 

            # 우선 이웃집 중 최고 높이를 할당 받을 max_height를 구한다.
            if near > max_height :
                max_height = near

        # 해당 집의 높이에서 이웃의 최고 높이인 max_height를 뺀 값이 0보다 커야 하고,
        # 그 값이 0보다 크다면 조망 세대 수인 view_house에 더해준다.
        view = heights[idx] - max_height
        if view > 0 :
            view_house += view
        
    print(f'#{test_count} {view_house}')