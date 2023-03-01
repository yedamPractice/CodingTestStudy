# 옹알이(1)
def solution(babbling):
    answer = 0
    s = ["aya","ye","woo","ma"]
    temp = []
    for i in range(len(s)):
        for j in range(len(s)):
            if j==i:
                continue
            temp.append(s[i]+s[j])
    temp1 =[]
    for a in temp:
        for b in s:
            if b in a:
                continue
            temp1.append(a+b)
    
    temp2=[]
    for c in temp1:
        for d in s:
            if d in c:
                continue
            temp2.append(c+d)
            
    possible = s + temp + temp1 + temp2

    
    for i in possible:
        if babbling.count(i)>=1:
            answer+=babbling.count(i)
    return answer


# 안전지대
def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    booms = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                booms.append((x, y))

    for x, y in booms:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1

    return count


# 겹치는 선분의 길이
def solution(lines):
    table = [set([]) for _ in range(200)] 
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) 

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1

    return answer


# 평행
def solution(dots):
    answer = 0
    if lean(dots[0],dots[1])==lean(dots[2],dots[3]):
        answer = 1
    if lean(dots[0],dots[2])==lean(dots[1],dots[3]):
        answer = 1
    if lean(dots[0],dots[3])==lean(dots[1],dots[2]):
        answer = 1
    return answer

def lean(dot1,dot2):
    return (dot2[1]-dot1[1])/(dot2[0]-dot1[0])