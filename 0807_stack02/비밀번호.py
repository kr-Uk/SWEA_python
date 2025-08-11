MSG_FORMAT = '#{} {}'

for test_case in range(1, 11):
    n, s = input().split()
    n = int(n)
    
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i -= 1
        else:
            i += 1
    print(MSG_FORMAT.format(test_case, s))