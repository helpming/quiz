def solution(order):
    # count = str(order).count('3')
    # count += str(order).count('6')
    # count += str(order).count('9')
    # return count
    return sum(list(map(lambda x: str(order).count(x), '369')))