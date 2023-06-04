burger_prices = []
for _ in range(3):
    burger_prices.append(int(input()))
    
drink_prices = []
for _ in range(2):
    drink_prices.append(int(input()))

# 가장 싼 햄버거 가격과 음료 가격을 찾아서 세트 메뉴의 가격을 계산
min_burger_price = min(burger_prices)
min_drink_price = min(drink_prices)
set_menu_price = min_burger_price + min_drink_price - 50

print(set_menu_price)
