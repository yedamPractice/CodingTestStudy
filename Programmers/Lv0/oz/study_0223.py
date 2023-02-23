#저주의 숫자3
def solution(n):
    i = 0
    result = 1
    while i < n:
        if result%3==0 or "3" in str(result):
            result += 1
        else:
            i += 1
            result += 1
    return result-1



# 외계어 사전
def solution(spell, dic):
    answer = 0
    arr=[]
    for i in range(len(dic)):
        count=0
        for j in spell:
            if j in dic[i]:
                count+=1
            arr.insert(i,count)
    if len(spell) in arr:
        answer = 1
    else:
        answer = 2
    return answer



# 유한소수 판별하기
from math import gcd
def solution(a, b):
    b /= gcd(a,b)
    
    while b%2==0:
        b/=2
    while b%5==0:
        b/=5
    
    if b in [1,2,5]:
        answer = 1
    else:
        answer = 2
    return answer



# 평행 (테스트 12번 부터 에러뜸..)
def solution(dots):
    arr = []
    
    for i in range(4):
        for j in range(4):
            if j <=i:
                continue
            else:
                arr.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))

    temp1 = set(arr)
    
    if len(temp1)==6:
        answer = 0
    else:
        answer = 1
    
    return answer