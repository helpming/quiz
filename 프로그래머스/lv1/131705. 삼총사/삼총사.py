def solution(number):
    answer = 0
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                # 세 학생의 정수 번호를 더해서 0이 되는 경우
                if number[i] + number[j] + number[k] == 0:
                    answer += 1  # 방법의 수 증가
    return answer