MSG_FORMAT = '#{} {}'

def dfs(k):
    if k == n:
        return True
    
    for i in range(n+1):
        if graph[k][i] == 1:
            if dfs(i):
                return True
    return False
for _ in range(10):
    test_case, n = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    ilst = list(map(int, input().split()))

    for i in range(0, n*2, 2):
        a, b = ilst[i], ilst[i+1]
        if b == 99:
            graph[a][n] = 1
            continue
        graph[a][b] = 1
    
    print(MSG_FORMAT.format(test_case, 1 if dfs(0) else 0))