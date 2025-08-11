MSG_FORMAT = '#{} {}'

for test_case in range(1, 11):
    trash = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for x in range(100):
        isN = False
        isS = False
        for y in range(100):
            if graph[y][x] == 1:
                isS = False
                isN = True 
            elif graph[y][x] == 2:
                if isN:
                    result += 1
                isS = True
                isN = False
    print(MSG_FORMAT.format(test_case, result))