# 초기화를 위해 가장 높은 온도로 설정
coldest_temperature = 201

# 가장 추운 도시를 저장할 변수 초기화
coldest_city = ""

# 입력 받기
while True:
    try:
        input_data = input().split()
        city = input_data[0]
        temperature = int(input_data[1])
        
        # 현재 가장 추운 도시와 온도와 비교
        if temperature < coldest_temperature:
            coldest_temperature = temperature
            coldest_city = city
    except EOFError:
        break

# 가장 추운 도시 출력
print(coldest_city)
