# 몫 구하기

def solution(num1, num2):
    answer = num1//num2
    return answer

# 두 수 나눗셈
def solution(num1, num2):
    answer = int(num1/num2*1000)
    return 
    

# 숫자 비교하기
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer


# 모음 제거
def solution(my_string):
    
    my_string = my_string.replace("a","")
    my_string = my_string.replace("e","")
    my_string = my_string.replace("i","")
    my_string = my_string.replace("o","")
    my_string = my_string.replace("u","")
    
    answer = my_string
    
    return answer

# 내가 하려던 풀이ㅋㅋㅋㅋ    
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string


# 팩토리얼
def solution(n):
    result = 1
    a = 10
    for i in range(1, a+1):
        result *= i 
        if result == n:
            answer = i
        elif result > n:
            answer = i-1
            break
    return answer

# 문자열 구하기(1)
def solution(my_string):
    
    result = []
    for i in my_string:
        if i.isdigit():
            result.append(i)
                
    result = list(result)
    result.sort()
    answer = list(map(int,result))
    return answer
