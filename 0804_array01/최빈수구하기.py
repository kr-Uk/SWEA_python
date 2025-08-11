MSG_FORMAT = '#{} {}'
t = int(input())

for _ in range(t):
    test_case = int(input())
    score = [0] * 101
    ilst = list(map(int, input().split()))
    
    for i in range(len(ilst)):
        score[ilst[i]] += 1
    
    temp = max(score)
    for i in range(100, 0, -1):
        if score[i] == temp:
            result = i
            break
        
    print(MSG_FORMAT.format(test_case, result))