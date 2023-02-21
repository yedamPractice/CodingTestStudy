# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = [numbers[-1]]+numbers[:-1]
    if direction == "left":
        answer = numbers[1:]+[numbers[0]]
    return answer

# 2차원 배열 만들기
import numpy as np

def solution(num_list, n):
    
    a = len(num_list)//n
    answer = np.reshape(num_list,(a,n))
    return answer.tolist()


# 다항식 더하기
def solution(polynomial):
    
    only_num=[]
    have_x=[]
    num=[]
    a = polynomial.replace(" ","").split("+")

    for i in a:
        if i.isdigit():
            only_num.append(int(i))
        else:
            have_x.append(i)
            
    for i in have_x:
        if i == "x":
            num.append(1)
        else:
            num.append(int(i[:-1]))
            
    b = sum(num)
    c = sum(only_num)
    
    if b==0:
        answer = str(c)
    elif b==1 and c==0:
        answer = "x"
    elif b==1 and c!=0:
        answer = "x"+" "+"+"+" "+str(c)
    elif b!= 0 and c==0:
        answer = str(b)+"x"
    else:
        answer = str(b)+"x"+" "+"+"+" "+str(c)

    return answer


# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    
    for i in list(my_string):
        if i.isalpha():
            my_string = my_string.replace(i," ")
    answer = my_string.split() 
    answer = map(int,answer)
    return sum(answer)




