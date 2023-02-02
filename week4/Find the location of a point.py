def solution(dot):
    answer = 0
    if dot[0]>0:
        if dot[1]>0:
            answer=1
        elif dot[1]<0:
            answer=4
            
    if dot[0]<0:
        if dot[1]>0:
            answer=2
        else:
            answer=3
    return answer