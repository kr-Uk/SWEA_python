MSG_FORMAT = '#{} {}'

t = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    max_depth = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] < graph[y][x]:
            depth = dfs(nx, ny) + 1
            max_depth = max(max_depth, depth)
    
    return max_depth

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    maximum = 0
    
    for i in range(n):
        maximum = max(max(graph[i]), maximum)
        
    max_coor = []
    for y in range(n):
        for x in range(n):
            if graph[y][x] == maximum:
                max_coor.append((x, y))
                
    for y in range(n):
        for x in range(n):
            for cut in range(k+1):
                graph[y][x] -= cut
                for mx, my in max_coor:
                    if mx == x and my == y:
                        continue
                    result = max(result, dfs(mx, my))
                graph[y][x] += cut
            
    print(MSG_FORMAT.format(test_case, result))