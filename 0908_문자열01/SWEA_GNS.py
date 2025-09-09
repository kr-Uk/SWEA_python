counting = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

printing = {
    0 : "ZRO",
    1 : "ONE",
    2 : "TWO",
    3 : "THR",
    4 : "FOR",
    5 : "FIV",
    6 : "SIX",
    7 : "SVN",
    8 : "EGT",
    9 : "NIN" 
}

t = int(input())

for _ in range(t):
    test_case, n = input().split()
    n = int(n)
    count = [0] * 10
    temp = list(input().split())
    
    for i in range(n):
        count[counting[temp[i]]] += 1
    
    print(test_case)
    for i in range(10):
        for _ in range(count[i]):
            print(printing[i], end = " ")
    print()