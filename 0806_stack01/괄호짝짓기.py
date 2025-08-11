MSG_FORMAT = '#{} {}'

for test_case in range(1, 11):
    n = int(input())
    ilst = list(input())
    stack = []
    result = 1
    dict = {'(':')', '[':']', '{':'}', '<':'>'}
    
    for i in ilst:
        if i in ['(', '[', '{', '<']:
            stack.append(i)
        else:
            if not stack:
                result = 0
                break
            temp = stack.pop()
            if dict[temp] != i:
                result = 0
                break

    print(MSG_FORMAT.format(test_case, result))