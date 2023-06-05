x = list(range(1, 31))
hw_list = []
for i in range(1, 29):
  i = int(input())
  hw_list.append(i)
result = list(set(x) - set(hw_list))
result = sorted(result)
for i in result:
  print(i)