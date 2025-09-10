"""
행렬

dn = max(dn-1 * matrixn, dn-2 * matrixn-1 * matrixn)
"""

MSG_FORMAT = '#{} {}'

def searchSize(x, y):
    cnt_x = x
    cnt_y = y
    
    while cnt_x < n and graph[y][cnt_x] != 0:
        cnt_x += 1
    
    while cnt_y < n and graph[cnt_y][x] != 0:
        cnt_y += 1
    
    for _y in range(y, cnt_y):
        for _x in range(x, cnt_x):
            graph[_y][_x] = 0
    
    return (cnt_y-y, cnt_x-x)

def sequenceSort(m):
    temp = []
    start_x = set()
    start_y = set()
    
    for x, y in m:
        start_x.add(x)
        start_y.add(y)
    
    start = start_x.pop()

    while True:
        for x, y in m:
            if x == start:
                temp.append((x, y))
                start = y
                break
        if len(temp) == len(m):
            break
    
    return temp

t = int(input())

for test_case in range(1, t+1):
    result = 0
    
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    matrix = []
    
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 0:
                matrix.append(searchSize(x, y))
    
    dp = [0] * (len(matrix)+1)
    matrix = sequenceSort(matrix)
    
    ################## 여기부터 ###
    dp[2] = matrix[0][0] * matrix[0][1] * matrix[1][1]
    if len(matrix) > 2:
        dp[3] = min(matrix[0][0] * matrix[0][1] * matrix[1][1] + matrix[0][0] * matrix[1][1] * matrix[2][1],
                    matrix[1][0] * matrix[1][1] * matrix[2][1] + matrix[0][0] * matrix[0][1] * matrix[2][1])
    
    # dp만 하기 !
    for i in range(4, n+1):
        dp[i] = min(dp[i-1] + matrix[0][0] * matrix[0][1] * matrix[1][1]) 
    
    print(MSG_FORMAT.format(test_case, result))