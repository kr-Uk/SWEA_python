MSG_FORMAT = '#{} {}'

t = int(input())

def findSlope(arr):
    visited = [0] * n
    for i in range(n-1):
        gap = arr[i] - arr[i+1]
        if gap >= 2:
            return 0
        if gap == 1:
            idx = i+1
            curr = arr[idx]
            for _ in range(k):
                if idx >= n or arr[idx] != curr or visited[idx]:
                    return 0
                visited[idx] = 1
                idx += 1

    for i in range(n-1, 0, -1):
        gap = arr[i] - arr[i-1]
        if gap >= 2:
            return 0
        if gap == 1:
            idx = i-1
            curr = arr[idx]
            for _ in range(k):
                if idx <= -1 or arr[idx] != curr or visited[idx]:
                    return 0
                visited[idx] = 1
                idx -= 1
    return 1

for test_case in range(1, t+1):
    result = 0
    n, k = map(int, input().split())
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    for row in graph:
        result += findSlope(row)
    
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(graph[y][x])
        result += findSlope(temp)
    
    print(MSG_FORMAT.format(test_case, result))