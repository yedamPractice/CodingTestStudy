# 중앙값 구하기
def solution(array):
    array.sort()
    n = len(array)
    num = int(n/2 -0.5)
    answer = array[num]
    return answer

def solution(array):
    array.sort()
    answer = array(len(array)//2)


# 짝수는 싫어요
def solution(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    answer = arr[0::2]
            
    return answer

def solution(n):
    arr = []
    for i in range(1,n+1):
        if i%2==1:
            arr.append(i)
    return arr

# 배열 원소의 길이
def solution(strlist):
    arr = []
    
    for i in strlist:
        arr.append(len(i))
        
    return arr

# 캐릭터의 좌표
'''def solution(keyinput, board):
    result = [0,0]
    left_board = -board[0]//2
    right_board = board[0]//2
    top_board = board[1]//2
    bottom_board = -board[1]//2
    
    for i in keyinput:
        if i == "left":
            result[0] -= 1
        elif i == "right":
            result[0] += 1
        elif i == "up":
             result[1] += 1
        else:
            result[1] -= 1
            
    if result[0]<left_board:
        result[0]=left_board
    if result[0]>right_board:
        result[0]=right_board
    if result[1]<bottom_board:
        result[1]=bottom_board
    if result[1]>top_board:
        result[1]=top_board
    
        
    return result'''

