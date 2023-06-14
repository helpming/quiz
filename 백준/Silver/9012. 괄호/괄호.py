n = int(input())
for i in range(n):
    ps = input()
    while True:
        if '()' not in ps:
            break
        ps = ps.replace('()', '')
    if ps == '':
        print('YES')
    else:
        print('NO')