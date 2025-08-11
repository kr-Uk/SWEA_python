MSG_FORMAT = '#{} {}'

def toPostfix(s):
    post = ''
    stack = []
    
    for i in range(n):
        if s[i] == '+':
            while len(stack) > 0 and stack[-1] != '(':
                post += stack.pop()
            stack.append('+')
        elif s[i] == '*':
            while len(stack) > 0 and stack[-1] != '+' and stack[-1] != '(':
                post += stack.pop()
            stack.append('*')
        elif s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            while stack[-1] != '(':
                post += stack.pop()
            stack.pop()
        else:
            post += s[i]
    while len(stack) != 0:
        post += stack.pop()
        
    return post

def getResult(s):
    stack = []
    i = 0
    
    for i in range(len(s)):
        if s[i] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif s[i] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        else:
            stack.append(int(s[i]))
    
    return stack[0]
            

for test_case in range(1, 11):
    result = 0
    n = int(input())
    infix = input()
    postfix = toPostfix(infix)
    result = getResult(postfix)
    print(MSG_FORMAT.format(test_case, result))