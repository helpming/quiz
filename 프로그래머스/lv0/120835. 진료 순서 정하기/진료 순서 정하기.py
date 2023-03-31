def solution(emergency):
    응급순서 = sorted(emergency, reverse=True)
    
    answer = [응급순서.index(응급도) + 1 for 응급도 in emergency]
    return answer