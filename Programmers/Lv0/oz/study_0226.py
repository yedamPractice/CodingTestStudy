# 특이한 정렬
def solution(numlist, n):
    answer = []
    temp = []
    
    numlist.sort(reverse=True)
    for i in numlist:
        temp.append(abs(i-n))
        
    tmp = temp.copy()
    
    for i in range(len(tmp)):
        a = temp.index(min(temp))
        answer.append(numlist[a])
        temp.pop(a)
        numlist.pop(a)
    
    return answer


# 등수 매기기

#런타임 에러ver(7,10)
def solution(score):
    
    average = []
    for i,j in score:
        average.append((i+j)/2)
   
    temp = average.copy()
    
    rank = 1

    while len(temp)!=0:
        a = average.index(max(temp))
        cnt = average.count(max(temp))
        if cnt == 1:
            average[a]=rank
            rank +=1
            temp.remove(max(temp))
        else:

            for i in range(cnt):
                average[a+i]=rank
                temp.remove(max(temp))
            rank += cnt
    return print(average)


def solution(score):
    
    average = []
    answer =[]
    for i,j in score:
        average.append((i+j)/len(score))
    
    temp = sorted(average,reverse=True)
    
    for i in average:
        answer.append(temp.index(i)+1)
        
    return answer

