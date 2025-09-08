MSG_FORMAT = '#{} {}'

def dfs(cnt, prev_coor, distance):
    global result
    if distance >= result:
        return
    if cnt == n:
        distance += abs(prev_coor[1]-end[1]) + abs(prev_coor[0]-end[0])
        result = min(result, distance)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, coor[i], distance+(abs(prev_coor[1]-coor[i][1]) + abs(prev_coor[0]-coor[i][0])))
            visited[i] = 0

t = int(input())

for test_case in range(1, t+1):
    result = 1e9
    n = int(input())
    temp = list(map(int, input().split()))
    coor = []
    
    for i in range(0, (n+2)*2, 2):
        if i == 0:
            start = (temp[i], temp[i+1])
        elif i == 2:
            end = (temp[i], temp[i+1])
        else:
            coor.append((temp[i], temp[i+1]))
    
    visited = [0] * n
    dfs(0, start, 0)
    
    print(MSG_FORMAT.format(test_case, result))