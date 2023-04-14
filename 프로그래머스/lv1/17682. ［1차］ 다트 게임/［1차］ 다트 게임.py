def solution(dartResult):
    점수 = []
    for index, value in enumerate(dartResult):
        if value == 'S':
            점수[-1] **= 1
        elif value == 'D':
            점수[-1] **= 2
        elif value == 'T':
            점수[-1] **= 3
        elif value == '*':
            점수[-1] *= 2
            if len(점수) >= 2:
                점수[-2] *= 2
        elif value == '#':
            점수[-1] *= -1
        else:
            if dartResult[index:index+2] == '10':
                점수.append(10)
            elif dartResult[index-1:index+1] != '10':
                점수.append(int(value))
    return sum(점수)
