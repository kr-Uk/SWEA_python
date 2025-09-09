"""
knapsack 0 1 문제
2차원 dp
"""

MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    result = 0
    n, l = map(int, input().split())
    gradient = []
    for _ in range(n):
        score, calorie = map(int, input().split())
        gradient.append((calorie, score))
    
    dp = [[0] * (l+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        c, s = gradient[i-1]
        for j in range(1, l+1):
            if c > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + s)

    print(MSG_FORMAT.format(test_case, dp[n][l]))