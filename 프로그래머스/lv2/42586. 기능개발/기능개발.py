from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            day = (100 - progress) // speed
            days.append(day)
        else:
            day = (100 - progress) // speed + 1
            days.append(day)
    while days:
        d = days.popleft()
        count = 1
        while days and d >= days[0]:
            days.popleft()
            count += 1
        if count > 0:
            answer.append(count)
    
    return answer