while True:
    word = input()
    if word == '.':
        break
    stack = []
    for i in word:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            stack.append(i)
        elif (i == ')' and stack and stack[-1] == '(') or (i == ']' and stack and stack[-1] == '['):
            stack.pop()
        else:
            stack.append(0)
            break
    print('no' if stack else 'yes')