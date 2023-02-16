# 순서쌍의 개수
def solution(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count +=1
        i +=1
    
    return count

# 개미군단
def solution(hp):
    
    five_a = hp//5
    hp = hp%5
    three_a = hp // 3
    hp = hp%3
    one_a = hp
    
    return five_a+three_a+one_a


# 진료 순서 정하기
'''def solution(emergency):
    arr = sorted(emergency)
    arr.reverse()
    n = len(emergency)
    for i in range(n):
        for j in range(n):
            if emergency[i] == arr[j]:
                emergency[i] = j+1
    
    
    return emergency'''

    
def solution(emergency):
    arr = sorted(emergency)
    arr.reverse()
    answer = []
    for i in emergency:
        answer.append(arr.index(i)+1)
    
    
    return answer


# 세균 증식
def solution(n, t):
    
    return n*2**t



# 문자열 배열하기(2)
def solution(my_string):
    answer = ""
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    for i in my_string:
        answer += i
    return answer



# 7의 개수
def solution(array):
    count = 0
    for i in array:
        a = str(i).count("7")
        count += a 
    return count

