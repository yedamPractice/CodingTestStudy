# 치킨 쿠폰
def solution(chicken):
    temp = 0
    coupon = 0
    while chicken>9:
        temp += chicken//10
        coupon += temp
        chicken = chicken%10 + temp
        temp = 0
    return coupon


# 다음에 올 숫자
def solution(common):
    answer = 0
    if (common[1] - common[0]) == (common[2] - common[1]):
        answer = common[-1] + (common[2] - common[1])
    else: 
        answer = common[-1]*(common[2]//common[1])
                                                      
    return answer


# 이진수 더하기
def solution(bin1, bin2):
    answer = ''
    a = int(bin1,2)
    b = int(bin2,2)
    answer = bin(a+b)
    return answer[2:]


# 연속된 수의 합
def solution(num, total):
    answer = []
    s= 0
    for i in range(num):
        s += i
    a = (total-s)//num
    
    for _ in range(num):
        answer.append(a)
        a += 1
    return answer