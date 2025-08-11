MSG_FORMAT = '#{} {} {}'


def dfs(x, y):
    global memo
    memo[graph[y][x]] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == graph[y][x] + 1:
            if memo[graph[ny][nx]] > 0:
                memo[graph[y][x]] = memo[graph[ny][nx]] + 1
            else:
                memo[graph[y][x]] = dfs(nx, ny)
            break
    
    return memo[graph[y][x]]+1

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    memo = [0] * (n**2+1)
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    for y in range(n): 
        for x in range(n):
            if memo[graph[y][x]] == 0:
                dfs(x, y)
    
    maximum = max(memo)
    room_num = memo.index(maximum)
    print(MSG_FORMAT.format(test_case, room_num, maximum))