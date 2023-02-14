# 특정 문자 제거하기
def solution(my_string, letter):
    answer = ''
    for c in my_string:
        if c == letter:
            continue
        answer += c
    return answer



# 각도기
def solution(angle):
    answer = 0
    if 0<angle<90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90<angle<180:
        answer = 3
    else:
        answer = 4
    return answer



# 양꼬치
def solution(n, k):
    answer = 0
    answer = n*12000 + ((k-(n//10)))*2000
    return answer



# 숫자 찾기
def solution(num, k):
    answer = 0
    n = str(num)
    for c in n:
        if c == str(k):
            answer = n.index(c)+1
            break
        else:
            answer = -1
    return answer


# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n == 0:
            answer.append(i)
    return answer


# 자릿수 더하기
def solution(n):
    answer = 0
    num = str(n)
    for i in num:
        answer += int(i)
    
    return answer