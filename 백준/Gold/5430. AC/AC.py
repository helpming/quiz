from collections import deque

n = int(input())

result = []

for i in range(n):
  orders = input()
  m = int(input())
  l = deque(input()[1:-1].split(','))
  if '' in l:
    l.remove('')
  else:
    pass
  r_count = 0
  for order in orders:
    if order == 'R':
      r_count += 1
    else:
      if m == 0:
        result.append('error')
        break  
      else:
        if r_count % 2 == 1:
          l.pop()
          m -= 1
        else:
          l.popleft()
          m -= 1
  else:
      if r_count % 2 == 1:
        l.reverse()
      result.append('[' + ','.join(l) + ']')

print('\n'.join(result))