chars = input()

bomb = input()

stack = []

for char in chars:
    stack.append(char)

    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = ''.join(stack)

if len(result) == 0:
    print('FRULA')
else:
    print(result)