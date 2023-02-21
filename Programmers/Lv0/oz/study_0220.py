# 점의 위치 구하기
def solution(dot):
    a = dot[0]
    b = dot[1]
    if a>0 and b>0:
        answer = 1
    elif a<0 and b>0:
        answer = 2
    elif a<0 and b<0:
        answer = 3
    elif a>0 and b<0:
        answer = 4
    return answer

# 직사각형의 넓이 구하기
def solution(dots):
    answer = 0
    if dots[0][1]==dots[1][1]:
        a = dots[0][0] - dots[1][0]
        b = dots[0][1] - dots[3][1]
    elif dots[0][1]==dots[2][1]:
        a = dots[0][0] - dots[2][0]
        b = dots[0][1] - dots[1][1]
    elif dots[0][1]==dots[3][1]:
        a = dots[0][0] - dots[3][0]
        b = dots[0][1] - dots[1][1]
   
    return abs(a*b)



# 최댓값 만들기(2) 
# 1) 런타임 에러뜸
def solution(numbers):
    answer = []
    for i in numbers:
        for j in numbers:
            if i == j:
                continue
            elif i<0 and j>0:
                continue
            elif i>0 and j<0:
                continue
            answer.append(abs(i*j))
    return max(answer)



