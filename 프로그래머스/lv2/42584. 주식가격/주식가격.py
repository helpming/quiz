from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)
    while que:
        count = 0
        p = que.popleft()
        for q in que:
            if p <= q:
                count += 1
            else:
                count += 1
                break     
        answer.append(count)
    return answer