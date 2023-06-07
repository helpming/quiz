numbers = []
while True:
  num = int(input())
  if num == 0:
    break
  numbers.append(num)

for number in numbers:
  if number == int(str(number)[::-1]):
    print('yes')
  else:
    print('no')