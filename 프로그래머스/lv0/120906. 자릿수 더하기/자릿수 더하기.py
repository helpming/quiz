def solution(n):
    # result = 0
    # for i in str(n):
    #     result += int(i)
    # return result
    return sum(map(int, str(n)))