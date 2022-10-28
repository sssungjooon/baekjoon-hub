# 총 10개의 테스트 케이스가 주어진다.
T = 10 
for test_count in range(1, T+1):
    # 테스트 케이스의 길이 N
    N = int(input())
    # 코드 인풋 받는다.
    code = input()
    # 후위표기식을 위한 스택
    stack = []
    # 결과를 이어 받을 result
    result = ''
    # 코드를 순회하며 이 값이 숫자인지 연산자인지 확인
    for i in code:
        if i.isdigit() : 
            result += i
        else:
            if i == '(' :
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    # 다 순회했을 때 아직 stack에 남아있는게 있다면 뽑아서 result로
    while stack:
        result += stack.pop()

    stack = []
    for i in result:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(i))

    last = stack.pop()
    print(f'#{test_count} {last}')