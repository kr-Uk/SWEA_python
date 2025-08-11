MSG_FORMAT = '#{} {}'

for test_case in range(1, 11):
    result = 0
    n = int(input())
    ilst = list(map(int, input().split()))
    for i in range(2, n-2, 1):
        maximum = max(ilst[i-2], ilst[i-1], ilst[i+1], ilst[i+2])
        result += ilst[i] - maximum if ilst[i] > maximum else 0
    
    print(MSG_FORMAT.format(test_case, result))