MSG_FORMAT = '#{} {}'

def dfs(x, y):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if graph[ny][nx] == '3':
                return True
            if graph[ny][nx] == '0' and not visited[ny][nx]:
                visited[ny][nx] = 1
                if dfs(nx, ny):
                    return True
    
    return False

for _ in range(10):
    test_case = int(input())
    graph = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for x in range(16):
        for y in range(16):
            if graph[y][x] == '2':
                visited[y][x] = 1
                print(MSG_FORMAT.format(test_case, 1 if dfs(x, y) else 0))