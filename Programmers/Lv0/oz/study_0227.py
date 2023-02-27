# A로 B만들기
def solution(before, after):
    answer = 0
    count = 0
    for i in before:
        if before.count(i)== after.count(i):
            count+=1
    if count == len(before):
        answer = 1
    else:
        answer = 0
    return answer



# k의 개수
def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        if str(k) in str(num):
            if str(num).count(str(k))==1:
                answer +=1
            else:
                answer +=str(num).count(str(k))
    return answer

# 로그인 성공
def solution(id_pw, db):
    answer = "fail"
    
    for i in range(len(db)):
        if id_pw[0]== db[i][0]:
            answer = "wrong pw"
            if id_pw[1]== db[i][1]:
                answer = "login"
        
    return answer

#DAY13
# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for i in my_string:
        if answer.count(i) == 1:
            continue
        answer += i
        
    return answer

#삼각형이 완성조건(1)
def solution(sides):
    answer = 0
    temp = sides.copy()
    temp.remove(max(temp))
    
    if sum(temp) <= max(sides):
        answer = 2
    else:
        answer = 1
    return answer


#DAY19
#중복된 숫자 개수
def solution(array, n):
    answer = 0
    answer = array.count(n)
        
    return answer

#머쓱이 보다 키큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer+=1
    return answer


#DAY20
#캐릭터의 좌표
def solution(keyinput, board):
    result = [0,0]
    
    right_board = board[0]//2
    left_board = -right_board
    top_board = board[1]//2
    bottom_board = -top_board
    
    for i in keyinput:
        if i == "left":
            result[0] -= 1
            if result[0] < left_board:
                result[0] += 1
        elif i == "right":
            result[0] += 1
            if result[0] > right_board:
                result[0] -=1
        elif i == "up":
             result[1] += 1
             if result[1] > top_board:
                result[1] -=1   
        else:
            result[1] -= 1
            if result[1] < bottom_board:
                result[1] +=1
 
    
        
    return result