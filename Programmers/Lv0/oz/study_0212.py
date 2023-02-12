# 나이 출력
def solution(age):
    answer = 0
    answer = 2022-age+1
    return answer




# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
            
    return num_list


# -> 뒤에서 부터 빼와서 다시 배열에 저장
def solution(num_list):
    result =[]
    while(num_list):
        result.append(num_list.pop())
    return result




# 문자열 뒤집기
def solution(my_string):
    answer = ''
    for char in my_string:
        answer = char + answer
    return answer




# 한번만 등장한 문자
def solution(s):
    answer = ''
    result = ''
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            answer += s[i]
    result = "".join(sorted(answer))
    return result




# 약수 구하기
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i == 0:
            answer.append(n//i)
    answer.sort()
    return answer





# 편지
def solution(message):
    answer = len(message)*2
    return answer







