N = int(input()) ## 입력값 받기
num = 1 ## 초기 숫자 1의 벌집 개수는 1개
for i in range(N):
    num += i*6  ## i 번째 겹인 벌집 개수는 6의 배수로 늘어남 (num : 벌집 개수 누적)
    if N <= num: ## 벌집 개수의 누적이 입력값보다 커지면
        print(i+1) ## (i+1)번 째 겹인 것이므로 출력!
        break