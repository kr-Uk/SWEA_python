MSG_FORMAT = '#{} {:.0f}'

import heapq

t = int(input())

for test_case in range(1, t+1):
    result = 0
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    
    union_set = set()
    node = set(i for i in range(n))
    distance = []
    
    graph = []
    for i in range(n):
        graph.append((x[i], y[i]))
    
    # 0부터 시작
    union_set.add(0)
    for i in range(1, n):
        d = e * ((graph[0][0] - graph[i][0]) ** 2 + (graph[0][1] - graph[i][1]) ** 2)
        heapq.heappush(distance, (d, i))
        
    while union_set != node:
        tmp = heapq.heappop(distance)
        if tmp[1] in union_set:
            continue
        result += tmp[0]
        union_set.add(tmp[1])
        for i in range(1, n):
            if i in union_set:
                continue
            d = e * ((graph[tmp[1]][0] - graph[i][0]) ** 2 + (graph[tmp[1]][1] - graph[i][1]) ** 2)
            heapq.heappush(distance, (d, i))
    
    print(MSG_FORMAT.format(test_case, result))