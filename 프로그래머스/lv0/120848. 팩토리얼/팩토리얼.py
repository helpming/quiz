import math

def solution(n):
    answer = 0
    while True:
        answer += 1
        if math.factorial(answer) > n:
            break
    return answer-1