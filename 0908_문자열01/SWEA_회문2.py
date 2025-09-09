MSG_FORMAT = '#{} {}'

def palinDrome(temp):
    global result
    
    dp = [[0] * 101 for _ in range(101)]
    
    for j in range(100):
        dp[j][j] = 1
    
    for k in range(99):
        if temp[k] == temp[k+1]:
            dp[k][k+1] = 2
    
    for l in range(2, 100, 1):
        for start in range(100-l):
            end = start + l
            if temp[start] == temp[end] and dp[start+1][end-1] > 0:
                dp[start][end] = dp[start+1][end-1] + 2
    
    for d in range(100):
        result = max(result, max(dp[d]))

for _ in range(10):
    test_case = int(input())
    result = 0
    graph = []
    for _ in range(100):
        graph.append(input())
    
    for i in range(100):
        temp = graph[i]
        palinDrome(temp)
        
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += graph[j][i]
        palinDrome(temp)
    
    print(MSG_FORMAT.format(test_case, result))
    