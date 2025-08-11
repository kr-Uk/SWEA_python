MSG_FORMAT = '#{} {}'

def dfs(honey, idx, cnt, k, temp, c):

    if cnt == k:
        if sum(temp) > c:
            return 0
        
        return sum(x**2 for x in temp)
    
    best = 0
    
    for j in range(idx, m):
        temp.append(honey[j])
        best = max(best, dfs(honey, j+1, cnt+1, k, temp, c))
        temp.pop()

    return best

t = int(input())

for test_case in range(1, t+1):
    n, m, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    
    for y1 in range(n):
        for x1 in range(n-m+1):
            for y2 in range(n):
                for x2 in range(n-m+1):
                    if y1 == y2 and abs(x2 - x1) < m:
                        continue
                    honey1 = graph[y1][x1:x1+m]
                    honey2 = graph[y2][x2:x2+m]
                    # 여기까지가 두 벌통 나눈 것.

                    best1 = 0
                    best2 = 0
                    
                    for k in range(1, m+1):
                        best1 = max(best1, dfs(honey1, 0, 0, k, [], c))
                        best2 = max(best2, dfs(honey2, 0, 0, k, [], c))
                        
                    result = max(result, best1 + best2)

    print(MSG_FORMAT.format(test_case, result))