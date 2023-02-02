# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer


# 두 수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer


#두 수의 곱
def solution(num1, num2):
    answer = num1 *num2
    return answer


# 주사위 개수
def solution(box, n):
    
    a = box[0]//n
    b = box[1]//n
    c = box[2]//n
    
    answer = a*b*c
    
    return answer

# 최댓값 구하기
def solution(numbers):
    n = len(numbers)
    
    if numbers[0]>numbers[1]:
        max1 = numbers[0]
        max2 = numbers[1]
    else :
        max1 = numbers[1]
        max2 = numbers[0]
        
        
    for i in range(n-2):
    
        if max1 < numbers[i+2]:
            max2 = max1
            max1 = numbers[i+2]
                
        else :
            max1 = max1
            
            if max2 < numbers[i+2]:
                max2 = numbers[i+2]
            
            else : 
                max2 = max2
        
    answer = max1*max2
"""그냥 정렬하고 곱하기 하면 되는데 어렵게 품;; ㅎㅎ ㅇㄹㅇ"""

# 합성수 구하기
def solution(n):
    count = n-1
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                count -= 1
                break
    answer = n - count - 1
    return answer