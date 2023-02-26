# 최빈값 구하기
def solution(array):
    temp = set(array)
    arr = {i : 0 for i in temp}
    for i in temp:
        arr[i]=array.count(i)
    cnt = arr.values()
    cnt = list(cnt)
    
    convert_arr = {v:k for k,v in arr.items()}
    
    n = 0
    for i in cnt:
        if i == max(cnt):
            n +=1
            
    if len(cnt) == 1:
        answer = array[0]
        
    elif n>=2:
        answer = -1
        
    else:
        answer = convert_arr.get(max(cnt))
        
    return answer


# 공던지기
def solution(numbers, k):
    answer = 0

    if len(numbers)%2==0:
        people = numbers[0::2]
        answer = people[(k%len(people))-1]
    
    else:
        people = numbers[0::2]+numbers[1::2]
        answer = people[(k%len(people))-1]
        
    return answer
            

    
# 최댓값 만들기(2)
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i <= j:
                continue
            if numbers[i]*numbers[j]>0:
                answer.append(abs(numbers[i]*numbers[j]))
            else:
                answer.append(numbers[i]*numbers[j])
    return max(answer)