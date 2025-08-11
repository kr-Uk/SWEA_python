MSG_FORMAT = '#{} {}'

for _ in range(10):
    test_case = int(input())
    maximum = -1e9
    graph = [list(map(int, input().split())) for _ in range(100)]
    
    # 행
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += graph[i][j]
        maximum = max(maximum, row_sum)
        
    # 열
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += graph[j][i]
        maximum = max(maximum, col_sum)
    
    # 대각선
    diag_sum = 0
    for i in range(100):
        diag_sum += graph[i][i]
    maximum = max(maximum, diag_sum)
    
    diag_sum = 0
    for i in range(100):
        diag_sum += graph[i][99-i]
    maximum = max(maximum, diag_sum)
    
    print(MSG_FORMAT.format(test_case, maximum))