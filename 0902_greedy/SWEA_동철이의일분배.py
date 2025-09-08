MSG_FORMAT = '#{} {:.6f}'

t = int(input())

def dfs(cnt, prob):
    global result
    if prob <= result:
        return
    
    if cnt == n:
        result = prob
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, prob * graph[cnt][i]/100)
            visited[i] = 0

for test_case in range(1, t+1):
    result = 0
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [0] * n
    dfs(0, 100)

    print(MSG_FORMAT.format(test_case, result))