number_list = []

for _ in range(10):
    number = int(input())
    number_list.append(number%42)

new_num = list(set(number_list))
print(len(new_num))