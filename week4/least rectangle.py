def solution(sizes):
    answer = 0
    height = []
    width = []
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        # print(width)
        height.append(min(sizes[i]))
        # print(height)
    answer=max(height)*max(width)    
    
    return answer