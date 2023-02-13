# 직각삼각형 출력하기

n = int(input())
for i in range(1,n+1):
    print("*"*i)



# 짝수 홀수 개수
def solution(num_list):
    answer = []
    c_left = 0
    c_right = 0
    for i in num_list:
        if i%2==0:
            c_left +=1
        else:
            c_right += 1
    answer.append(c_left)
    answer.append(c_right)
    return answer


# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for c in my_string:
        answer = answer + c*n
    return answer


# 가장 큰 수 찾기
def solution(array):
    maxx = 0
    for i in array:
        if i>maxx:
            maxx = i
    return [maxx,array.index(maxx)]

    

# 배열의 유사성 찾기
def solution(s1, s2):
    count = 0
    for i in s1:
        for j in s2:
            if i == j:
                count += 1 
    return count


# 문자열 계산하기
def solution(my_string):
    
    return eval(my_string)