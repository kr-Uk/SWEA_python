MSG_FORMAT = '#{} {}'

nums = {
    "211" : 0,
    "221" : 1,
    "122" : 2,
    "411" : 3,
    "132" : 4,
    "231" : 5,
    "114" : 6,
    "312" : 7,
    "213" : 8,
    "112" : 9
}

hex2bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}


def cipher(code, x):
    code = code[:x+1]
    code = code[::-1] # 편하게 반전하기
    idx = 0
    result = []

    for _ in range(8):
        a, b, c= 0, 0, 0
        while code[idx] != '0':
            c += 1
            idx += 1
        while code[idx] != '1':
            b += 1
            idx += 1
        while code[idx] != '0':
            a += 1
            idx += 1
        while idx < len(code) and code[idx] != '1':
            idx += 1

        if a == 0 or b == 0 or c == 0:
            continue
        divide = min(min(a, b), c)
        
        key = str(a//divide) + str(b//divide) + str(c//divide)

        result.append(nums[key])

    result = result[::-1]
    answer = 0
    odd_sum = 0
    even_sum = 0
    for i in range(1, 8):
        if i % 2 == 1:
            odd_sum += result[i-1]
        else:
            even_sum += result[i-1]
    if ((odd_sum * 3) + even_sum + result[-1]) % 10 == 0:
        answer = odd_sum  + even_sum + result[-1]

    return (answer, divide * 56)

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    result = 0
    graph = []

    for _ in range(n):
        inp = input()
        temp = ''
        for t in inp:
            temp += hex2bin[t]
        graph.append(temp)

    for y in range(1, n):
        x = m*4-1
        while x > 54:
            if graph[y][x] == '1' and graph[y-1][x] != '1':
                code = graph[y][:]
                r, c = cipher(code, x)
                result += r
                x -= c
            x -= 1

    print(MSG_FORMAT.format(test_case, result))