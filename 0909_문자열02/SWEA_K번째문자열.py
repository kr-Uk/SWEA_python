t = int(input())

for test_case in range(1, t+1):
    result = ''
    k = int(input())
    word = input().rstrip()
    substring = set()
    
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring.add(word[i:j])
            
    print('#{} {}'.format(test_case, sorted(list(substring))[k-1]))