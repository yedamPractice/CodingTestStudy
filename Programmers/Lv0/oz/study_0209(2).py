# 배열의 평균 값
def solution(numbers):
    tmp = 0
    for i in numbers:
        tmp += i
    answer = tmp/len(numbers)
    
    return answer


# 옷 가게 할인받기
def solution(price):
    if 100000<=price<300000:
        answer = price*0.95
    elif 300000<=price<500000:
        answer = price*0.9
    elif price>=500000:
        answer = price*0.8
    else:
        return price
    return int(answer)

# 아이스 아메리카고
def solution(money):
    answer = []
    answer.append(money//5500)
    answer.append(money%5500)
    return answer


# 대문자와 소문자
def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer += s.lower()
        else:
            answer += s.upper()
            
    return answer


# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    a = my_string[num1]
    b = my_string[num2]
    my_string[num1] = b
    my_string[num2] = a

    return answer.join(my_string)

# 영어가 싫어요
def solution(numbers):
    answer = 0
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for index,n in enumerate(num):
        numbers = numbers.replace(n,str(index))
            
    return int(numbers)


