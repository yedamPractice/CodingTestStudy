# 가위 바위 보
def solution(rsp):
    answer = ""
    for i in rsp:
        if i == "2":
            answer+= "0"
        elif i == "0":
            answer += "5"
        else:
            answer += "2"
    return answer


# 모스 부호
def solution(letter):
    answer = ''
    mos =  { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    arr = letter.split()
    for i in arr:
        if i in mos.keys():
            answer += mos[i]
    return answer



# 구슬을 나누는 경우의 수
import math

def solution(balls, share):
    answer = 0
    a = math.factorial(balls)
    b = math.factorial(share)
    c = math.factorial(balls-share)
    
    answer = a/(b*c)
    return answer




# 종이 자르기
def solution(M, N):
    answer = 0
    a = M-1
    b = (N-1)*M
    answer = a+b
    return answer



# 잘라서 배열로 저장하기
def solution(my_str, n):
    
    s = ""
    for i in range(1,len(my_str)+1):
        if not i %n==0:
            s+=my_str[i-1]
        if i %n ==0:
            s+= my_str[i-1] + "\n"
    answer = s.split()
        
    return answer



# 문자열 밀기
def solution(A, B):
    n=0
    while n<len(A):
        if A==B:
            return n
        A = A[-1] + A[:-1]
        n += 1
    return -1