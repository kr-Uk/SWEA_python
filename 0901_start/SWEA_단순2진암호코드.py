MSG_FORMAT = '#{} {}'

nums = {
  "0001101" : 0,
  "0011001" : 1,
  "0010011" : 2,
  "0111101" : 3,
  "0100011" : 4,
  "0110001" : 5,
  "0101111" : 6,
  "0111011" : 7,
  "0110111" : 8,
  "0001011" : 9
}

t = int(input())

for test_case in range(1, t+1):
  result = 0
  n, m = map(int, input().split())
  graph = [input() for _ in range(n)]
  find = False
  code = ''
  start_idx = 0

  for row in graph:
    if find:
      break
    for i in range(m):
      if row[i] == '1':
        code = row[:]
        start_idx = i
        find = True
        break
  
  end_idx = start_idx + 55
  while True:
    if code[end_idx] == '1':
      break
    else:
      end_idx -= 1

  start_idx -= 56 - (end_idx - start_idx + 1)
  code = code[start_idx:end_idx+1]
  idx = 7
  odd_sum = 0
  even_sum = 0

  for i in range(1, 9):
    if i % 2 == 1:
      odd_sum += nums[code[idx-7:idx]]
    else:
      even_sum += nums[code[idx-7:idx]]
    idx += 7
    
  if (3 * odd_sum + even_sum) % 10 == 0:
    result = odd_sum + even_sum
  else:
    result = 0

  print(MSG_FORMAT.format(test_case, result))