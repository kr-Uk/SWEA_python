MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 13
    
    for i in range(1, 13):
        dp[i] = min(dp[i-1] + (fee[0] * plan[i-1]), dp[i-1] + fee[1]) # 1일권 vs 한달권
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3]+fee[2])
        if i == 12:
            dp[i] = min(dp[i], fee[3])
    
    print(MSG_FORMAT.format(test_case, dp[12]))