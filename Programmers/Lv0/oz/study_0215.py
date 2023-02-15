# 짝수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2==0:
            answer+=i
    return answer



# 배열 자르기
def solution(numbers, num1, num2):
    answer = []
    answer = numbers[num1:num2+1]
    return 
    

# 외계행성의 나이
def solution(age):
    alpha = "abcdefghij"
    age = str(age)
    answer = ""
    for i in age:
        answer += alpha[int(i)]
    return answer




# 문자열 안에 문자열
def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer



# 제곱수 판단하기
def solution(n):
    i = 1
    while True :
        if n > i**2:
            i += 1
        if n == i**2:
            return 1
            break
        if n < i**2:
            return 2
            break


# OX게임
def solution(quiz):
    answer = []
    for i in quiz:
        formula = i.split()
        if formula[1] == "+":
            if int(formula[0]) + int(formula[2]) == int(formula[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif formula[1] == "-":
            if int(formula[0]) - int(formula[2]) == int(formula[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer


