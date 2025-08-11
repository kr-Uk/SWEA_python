MSG_FORMAT = '#{} {}'

for test_case in range(1, 11):
    result = -1
    n = int(input())
    ilst = list(map(int, input().split()))
    for _ in range(n):
        mx = max(ilst)
        mn = min(ilst)
        if mx - mn <= 1:
            break
        
        ilst[ilst.index(mx)] -= 1
        ilst[ilst.index(mn)] += 1    

    result = max(ilst) - min(ilst)
    print(MSG_FORMAT.format(test_case, result))