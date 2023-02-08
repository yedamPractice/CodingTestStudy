# 피자 나눠 먹기(1)
def solution(n):
    if n % 7==0:
        answer = n//7
    else:
        answer = n//7+1
    return answer


# 피자 나눠 먹기(2)
def solution(n):
    for i in range(1,301):
        if i%6==0 and i%n==0:
            answer = i//6
            break
        
    return answer


# 피자 나눠 먹기(3)
def solution(slice, n):
    if n%slice == 0:
        answer = n//slice
    else:
        answer = n//slice + 1
    return answer


# 369게임
def solution(order):
    order = str(order)

    clap = 0
    for i in order:
        
        if int(i)%3==0 and int(i)!=0:
            clap += 1 
            
    return clap

# 암호 해독
def solution(cipher, code):
    answer = ""
    for i in range(1,len(cipher)+1):
        if i%code==0:
            answer += cipher[i-1]
    return answer

# 가까운 수
def solution(array, n):
    array.sort()
    answer = []
    
    for i in array:
        answer.append(abs(i-n))
    index = answer.index(min(answer))
    
    return array[index]
    
