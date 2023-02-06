# 배열 두 배 만들기
def solution(numbers):
    
    length = len(numbers)
    for i in range(length):
        numbers[i] = numbers[i]*2
    answer = numbers
    return answer


# 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer

# 분수의 덧셈
import math 

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = denom1*denom2
    b = numer1*denom2 + numer2*denom1
    
    n = math.gcd(a,b)
    
    answer.append(b//n)
    answer.append(a//n)
    return answer



# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    num = 0
    n = 0
    for i in my_string:
        if i.isdigit():
            num = int(i)
            if num > 0:
                n += int(i)
    
    return n


# 컨트롤 제트
def solution(s):
    
    s = s.split()
    
    n = 0
    
    for i in range(len(s)):
        
        if s[i] == "Z":
            n -= int(s[i-1])
        else:
            n += int(s[i])
        
    return n



# 소인수 분해
def solution(n):
    a = 2
    num = []
    while n >= a:
        if n % a == 0:
            num.append(a)
            n = n / a
        else:
            a = a + 1
    s = set(num)
    s = list(s)
    return s

def solution(n):
    a = 2
    num = []
    answer = []
    while n >= a:
        if n % a == 0:
            num.append(a)
            n = n // a
        else:
            a = a + 1
    for items in num:
        if items not in answer:
            answer.append(items)
            
    return answer

